#!/usr/bin/env python3

import sys, getopt
import requests

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.0                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

def help_func():
   print(f"""\033[0;31m<\033[0;37mHATAKE\033[0;31m> \033[0;37mVer.:1.0.0
=========================
Usage:
\033[0;31m------\033[0;37m
   \033[0;33m>>\033[0;37m python3 hatake.py -a <IPV4> | Get information about an IPv4 address
   \033[0;33m>>\033[0;37m python3 hatake.py | Get information about your public IPv4 address
   """)

def hatake(argv):
   ipver4 = ""

   try:
      opts, args = getopt.getopt(argv, "ha:", ["ipa="])
   except getopt.GetoptError:
      print("\033[0;37m[\033[0;31m+\033[0;37m] Usage: python3 hatake.py -a <IPV4>")
      sys.exit(1)

   for opt, arg in opts:
      if opt == '-h' or opt == '--help':
         help_func()
         sys.exit(0)
      elif opt in ("-a", "--ipa"):
         ipver4 = arg
      else:
         raise getopt.GetoptError(
            "\033[0;37m[\033[0;31m+\033[0;37m] Usage: python3 hatake.py -a <IPV4>"
         )

   tstart = datetime.now()

   print(
      f"\033[0;37m[\033[0;31m+\033[0;37m] Starting at {datetime.now()}\n" +
      f"\033[0;33m=" * 45
   )

   try:
      if ipver4 == "":
         print("\033[0;37m[\033[0;31m+\033[0;37m] Usage: python3 hatake.py -a <IPV4>")
         sys.exit(1)

      response = requests.get(
         f"""http://ip-api.com/json/{ipver4}?fields=status,message,continent,
           continentCode,country,countryCode,region,regionName,city,district,
           zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,
           proxy,hosting,query"""
      ).json()

      lst = list(response.items())

      for lst_items, frmt in lst:
         if lst_items == "lat":
            print(
               f"\033[0;37m", lst_items,
               " \033[0;33m>> \033[0;37m",
               frmt
            )
         elif lst_items == "lon":
            print(
               f"\033[0;37m",
               lst_items,
               " \033[0;33m>> \033[0;37m",
               frmt
            )
         else:
            print(
               f"\033[0;37m",
               lst_items,
               " \033[0;31m>> \033[0;37m",
               frmt
            )
   except KeyboardInterrupt:
      print(f"\n\033[0;37m[\033[0;31m+\033[0;37m] Ctrl+C pressed. EXITING.")
      sys.exit(1)
   except requests.RequestException as reqexc:
      print(f"\033[0;37m[\033[0;33m-\033[0;37m] An error was defined!\n{reqexc}")
      sys.exit(1)
   except Exception as error:
      print(f"\033[0;37m[\033[0;33m-\033[0;37m] An error was defined!\n{error}")
      sys.exit(1)

   tend = datetime.now()

   print(
      f"\033[0;33m=\033[0;37m" * 45,
      f"\n\033[0;37m[\033[0;31m+\033[0;37m] Hatake done in {tend - tstart}"
   )


if __name__ == "__main__":
   from termcolor import colored
   from datetime import datetime
   import pyfiglet

   print(
      colored(
         pyfiglet.figlet_format(
            "hatake",
            font='bulbhead'
         ), "red"
      )
   )

   hatake(sys.argv[1:])
