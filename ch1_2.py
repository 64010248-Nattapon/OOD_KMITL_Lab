print(" *** Wind classification *** ")
sp=float(input("Enter wind speed (km/h) : "))
if sp>=0 and sp<=51.99:
    print("Wind classification is Breeze.")
elif sp>=52.00 and sp<=55.99:
    print("Wind classification is Depresstion.")
elif sp>=56.00 and sp<=101.99:
    print("Wind classification is Tropical Storm.")
elif sp>=102.00 and sp<=208.99:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")