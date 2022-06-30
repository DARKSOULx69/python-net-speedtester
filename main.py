# import libraries
from speedtest import Speedtest

print("""
 ___  ____  ____  ____  ____  ____  ____  ___  ____ 
/ __)(  _ \( ___)( ___)(  _ \(_  _)( ___)/ __)(_  _)
\__ \ )___/ )__)  )__)  )(_) ) )(   )__) \__ \  )(  
(___/(__)  (____)(____)(____/ (__) (____)(___/ (__) c1.0
                 by Chamod Savinda                                    
          https://github.com/DARKSOULx69
""")

# bits/ps to bps, kbps, mbps, MBps, GBps
scales = [
    (1024 ** 3, ' GB'), 
    (1024 ** 2, ' MB'), 
    (1024 ** 1, ' KB'),
    (1024 ** 0, (' byte', ' bytes')),
    ]

def size(bytes, system= scales):
    for factor, suffix in system:
        if bytes >= factor:
            break
    amount = int(bytes/factor)
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix

# calculate download speed
print("\nCalculating Download Speed...")
dspeed= Speedtest().download()
dspeed= float(dspeed)
dspeed= size(dspeed)

print(f"Download Speed: {dspeed}ps")

# calculate upload speed
print("\nCalculating Upload Speed...")
uspeed= Speedtest().upload()
uspeed= float(uspeed)
uspeed= size(uspeed)

print(f"Upload Speed: {uspeed}ps")

# get ping
print("\nGetting Ping...")
ping= Speedtest().results.ping

print(f"{ping}ms")