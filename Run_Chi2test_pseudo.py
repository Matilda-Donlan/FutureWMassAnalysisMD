import ROOT
import yaml
import csv


def calc_chi_square(nominal,histogram):
    if histogram.GetNbinsX()!= nominal.GetNbinsX():
        exit(1)
        #print ("bin cont. nominal","+/- bin err.","|| bin cont. test","+/- bin. err","||Sum(chi-square)")
    chi_square= (histogram.GetBinContent(1)-nominal.GetBinContent(1))**2 / (histogram.GetBinError(1)**2 + nominal.GetBinError(1)**2)
    for i in range(2, histogram.GetNbinsX()+1):
        E_i = nominal.GetBinContent(i)
        O_i = histogram.GetBinContent(i)
        sigma_E_i = nominal.GetBinError(i)**2
        sigma_O_i = histogram.GetBinError(i)**2

        # Avoid division by zero
        if E_i != 0:
            #print(E_i,nominal.GetBinError(i),O_i,"||",histogram.GetBinError(i),"||",chi_square)
            chi_square = chi_square + (O_i - E_i) ** 2 /(sigma_E_i+sigma_O_i) 
        else:
            # You can handle this case in different ways. Here we skip the bin.
            print(f"Skipping bin {i} because expected value is zero.")
       

    return chi_square

def read_config(config_file):
    """
    read YAML configuration
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load configuration from YAML file                                                                                                                                                           
config = read_config('pseudoConfigStat.yaml')

# Extract configuration values                                                                                                                                                                
root_file_name = config['root_file']
nominal_hist_name = config['nominal_histogram']
distribution_for_test = config['distribution']
histograms_to_compare = config.get('histograms_to_compare', [])
luminosity = config.get('luminosity', None)
output_csv =  f"outputChi2_{distribution_for_test}.csv"

# Open the ROOT file                                                                                                                                                                          
file = ROOT.TFile.Open(root_file_name)

# Retrieve the nominal histogram
print(f"Nominal is hist_{distribution_for_test}_{nominal_hist_name}")
nominal_hist = file.Get(f"hist_{distribution_for_test}_{nominal_hist_name}")

# Check if the nominal histogram exists                                                                                                                                                       
if not nominal_hist:
    print(f"Nominal histogram '{nominal_hist_name}' not found in file")
    exit(1)

# Generate pseudodata using the expected values
pseudodata_hist = nominal_hist.Clone()
pseudodata_hist.Reset()
print(nominal_hist)
pseudodata_hist.FillRandom(nominal_hist, 10_000_000) # Fixed cross-section of 10 ab-1



# Open CSV file for writing
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write CSV header
    #csvwriter.writerow(['W_mass', 'Chi2','Hand_Calc_Chi2'])
    csvwriter.writerow(['Wmass', 'Chi2',' Pvalue'])



    # Loop over all histograms you want to compare nominal to
    for hist_name in histograms_to_compare:
        hist = file.Get(f"hist_{distribution_for_test}_{hist_name}")

        if not hist:
            print(f" Histogram 'hist_{distribution_for_test}_{hist_name}' not found in file")
            continue
        hand_calculation = calc_chi_square(nominal_hist,hist)
        print("chi-square (bin-by-bin)=",hand_calculation)
        
        #chi2 = nominal_hist.Chi2Test(hist, "CHI2")
        #p_value = nominal_hist.Chi2Test(hist, "P")
        chi2 = pseudodata_hist.Chi2Test(hist, "UW CHI2")
        p_value = pseudodata_hist.Chi2Test(hist, "UW P")



        csvwriter.writerow([hist_name, chi2,hand_calculation])
        # Print results                                                                                                                                                                       
        #print(f"Comparing nominal histogram (hist_{distribution_for_test}_{nominal_hist_name}) with 'hist_{distribution_for_test}_{hist_name}':")
        print(f"Comparing pseudodata histogram (hist_{distribution_for_test}_{nominal_hist_name}) with 'hist_{distribution_for_test}_{hist_name}':")
        print(f"Chi2: {chi2}")
        print(f"p-value: {p_value}")
        
        
# Close the file                                                                                                                                                                              
file.Close()
