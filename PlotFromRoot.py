import ROOT
import argparse

from functools import partial

from analysis import config
from analysis import Sample
from analysis import ExampleAnalysis

from kkconfig import runconfig

from kkroot import style
from kkroot import canvas

def plot_and_save_TH1(hname, *args, ratio=None):
    """
    Plot and save 1D histograms.

    The histograms of all samples are added to a single
    THStack and then plotted on a canvas. The canvas is saved
    as a PNG file.
    """
    # Create a canvas
    c = ROOT.TCanvas()

    if ratio is None:
        pad,pad_ratio = c,None
    else:
        pad,pad_ratio = canvas.apply_ratio_canvas_style(c)

    # Get a histogram type to determine common useful things
    exhist=getattr(args[0],hname)

    # Create THStack
    hs = ROOT.THStack(f"hs_{hname}", '')
    hs_ratio = ROOT.THStack(f"hs_ratio_{hname}", '')

    # Get reference histogram for ratios
    h_ref = getattr(args[ratio.get('reference',0)], hname) if ratio is not None else None

    # Create and style the histogram
    for histobj in args:
        # Add and style histogram
        hist=getattr(histobj, hname)
        style.style(hist,**histobj.style)
        hs.Add(hist, 'HIST')

        # Add the ratio plot
        if h_ref is not None:
            hrat=hist.Clone()
            hrat.Divide(h_ref)
            hs_ratio.Add(hrat, 'E')

    # Draw stack
    pad.cd()
    hs.Draw("nostack")
    hs.GetXaxis().SetTitle(exhist.GetXaxis().GetTitle())
    hs.GetYaxis().SetTitle(exhist.GetYaxis().GetTitle())
    pad.BuildLegend(0.7,0.95-0.07*len(args),0.95,0.95)
    pad.Update()

    # Draw ratio (if requested)
    if pad_ratio is not None:
        pad_ratio.cd()
        hs_ratio.Draw("nostack")
        hs_ratio.GetXaxis().SetTitle(exhist.GetXaxis().GetTitle())
        canvas.apply_ratio_axis_style(hs_ratio)

        style.style(hs_ratio, **ratio)

        pad_ratio.Update()

    # Save the canvas as a PNG file
    c.SaveAs(f'{hname}.png')

def plot_and_save_TH2(hname, *args):
    """
    Plot and save 2D histograms.

    The histograms for each sample are plotted independently and
    saved with the title of the sample in the filename.
    """
    # Create a canvas
    c = ROOT.TCanvas()

    # Create and style the histogram
    for histobj in args:
        c.Clear()

        # Add and style histogram
        hist=getattr(histobj, hname)
        style.style(hist,**histobj.style)

        # Draw the histogram
        hist.Draw('COLZ')

        # Save the canvas as a PNG file
        c.SaveAs(f'{hname}_{histobj.title}.png')

def write_to_root(*args):                                                                                                                                                          
    """                                                                                                                                                                                      
    Writes all histograms in a common root file                                                                                                                                              
    writes seperate histograms for each W mass                                                                                                                                               
    this root file will be the input for the chi2 test                                                                                                                                       
    """ 
    f = ROOT.TFile("histograms.root","RECREATE")

    for hobj in args:

        hnames=filter(lambda key: key.startswith('hist'), dir(hobj))
        
        for hname in hnames:
            hist=getattr(hobj,hname)
            hobjname=hobj.title
            hobjname=hobjname.replace(" GeV","")
            hist.Write(f"{hname}_{hobjname}")    
    f.Close()
    
def plot_and_save(*args, ratio=None):
    """
    Creates a THStack to overlay the histograms inside `*args, draws the
    stack on a canvas, and saves the plot as a PNG file.
    """

    #
    # Get a list of histograms

    hnames=filter(lambda key: key.startswith('hist'), dir(args[0]))
    
    for hname in hnames:
        print(f'Plotting {hname}')
        # Create a canvas
        c = ROOT.TCanvas()
        
        # Get a histogram type to determine common useful things
        exhist=getattr(args[0],hname)

        if exhist.InheritsFrom('TH2'):
            plot_and_save_TH2(hname, *args)
        elif exhist.InheritsFrom('TH1'):
            plot_and_save_TH1(hname, *args, ratio=ratio)

def main(runconfig_path, nevents=-1):
    """
    Main function to read tree contents, create distributions, and plot/save 
    the histograms.
    """

    runcfg=runconfig.load([runconfig_path])

    samples=[]
    for input in runcfg.get('inputs',[]):

        sample=Sample.Sample(input.get('title',''))

        path=input.get('path',[])
        if type(path) is not list:
            path=[path]

        for p in path:
            # Relative paths should be relative to datadir
            if not p.startswith('/'):
                p=f'{config.datadir}/{p}'
            # Add file to the sample
            sample.add_file(p)
        sample.style=input.get('style', {})
        sample.crosssection=input.get('crosssection', 1)
        sample.open()

        samples.append(sample)

    analysis=ExampleAnalysis.ExampleAnalysis()

    hists=map(partial(analysis.run, nevents=nevents), samples)

    hists_list = list(hists)

    write_to_root(*hists_list)
    plot_and_save(*hists_list, ratio=runcfg.get('ratio', None))

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="script that reads root files to create and plot distributions.")
    parser.add_argument("runconfig", type=str, help="Path to the run configuration YAML file.")
    parser.add_argument("-n", "--nevents", type=int, default=-1, help="Maximum number of events to process per sample..")

    ROOT.gInterpreter.AddIncludePath(f"{config.mg5amcnlo}/Delphes");
    ROOT.gInterpreter.AddIncludePath(f"{config.mg5amcnlo}/Delphes/external");

    ROOT.gSystem.Load(f'{config.mg5amcnlo}/Delphes/libDelphes.so')
    
    # Parse the arguments
    args = parser.parse_args()

    # Execute the main function with the provided arguments
    main(args.runconfig, nevents=args.nevents)
