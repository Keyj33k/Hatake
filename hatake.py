#!/usr/bin/env python3

try:
    import sys
    import getopt
    from termcolor import colored
    from datetime import datetime
    import pyfiglet
    import requests
except ImportError:
    raise RuntimeError("Failed to import important modules.EXIT!")


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.1                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

def help_func():
    print(f"""\033[0;31m<\033[0;37mHATAKE\033[0;31m> | \033[0;37mPython\033[0;31m-\033[0;37m3\033[0;31m.\033[0;37m10\033[0;31m.\033[0;37m4 \033[0;31m| \033[0;37mVer\033[0;31m.:\033[0;37m1\033[0;31m.\033[0;37m0\033[0;31m.\033[0;37m0
\033[0;33m==================================================\033[0;37m
\nUsage:
\033[0;31m------\033[0;37m
   \033[0;33m>>\033[0;37m python3 hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37ma\033[0;31m/--\033[0;37maddr \033[0;31m<\033[0;37mIPV4\033[0;31m> \033[0;31m|\033[0;37m get information about a given IPv4 address
   \033[0;33m>>\033[0;37m python3 hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mp\033[0;31m/--\033[0;37mpipa \033[0;31m|\033[0;37m get your public ipv4 address
\nOptional:
\033[0;31m---------\033[0;37m
   \033[0;33m>>\033[0;37m python3 hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mh\033[0;31m/--\033[0;37mhelp \033[0;31m|\033[0;37m show help page
   """)


def public_ipv4_request():
    print(
        f" \033[0;37m[\033[0;31m*\033[0;37m] Written by \033[0;31m@\033[0;37mKeyj33k\n",
        f"\033[0;37m[\033[0;31m+\033[0;37m] Starting Hatake at {datetime.now()}\n",
        f"\033[0;33m=" * 50
    )

    tstart = datetime.now()

    try:
        print(
            f" \033[0;37m[\033[0;31m+\033[0;37m] Your Public ",
            f"IPv4\033[0;31m:\033[0;37m\t{requests.get('https://api.ipify.org').text}"
        )
    except requests.RequestException as reqexc:
        print(reqexc)

    tend = datetime.now()

    print(
        " " + f"\033[0;33m=\033[0;37m" * 50,
        f"\n \033[0;37m[\033[0;31m+\033[0;37m] Hatake done in {tend - tstart}"
    )


def api_request(ipver4):
    tstart = datetime.now()

    print(
        f" \033[0;37m[\033[0;31m*\033[0;37m] Written by \033[0;31m@\033[0;37mKeyj33k\n",
        f"\033[0;37m[\033[0;31m+\033[0;37m] Starting Hatake at {datetime.now()}\n",
        f"\033[0;33m=" * 50
    )

    try:
        if len(ipver4) == 0:
            print(
                f" \033[0;37m[\033[0;31m*\033[0;37m] Usage\033[0;31m:\033[0;37m python3 ",
                f"hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mh"
            )
            sys.exit(1)

        response = requests.get(
            f"""http://ip-api.com/json/{ipver4}?fields=status,message,continent,
            continentCode,country,countryCode,region,regionName,city,district,
            zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,
            proxy,hosting,query"""
        ).json()

        lst = list(response.items())

        print(f" \033[0;37m[\033[0;31m*\033[0;37m] Results:")
        print(" " + "-" * 12)

        for lst_items, frmt in lst:
            if lst_items == "lat":
                print(
                    f"\t\033[0;37m[\033[0;32m+\033[0;37m]\033[0;37m",
                    f"\033[0;37m", lst_items,
                    f" \033[0;33m>> \033[0;37m",
                    frmt
                )
            elif lst_items == "lon":
                print(
                    f"\t\033[0;37m[\033[0;32m+\033[0;37m]\033[0;37m",
                    f"\033[0;37m",
                    lst_items,
                    f" \033[0;33m>> \033[0;37m",
                    frmt
                )
            else:
                print(
                    f"\t\033[0;37m[\033[0;32m+\033[0;37m]\033[0;37m",
                    f"\033[0;37m",
                    lst_items,
                    f" \033[0;31m>> \033[0;37m",
                    frmt
                )
    except KeyboardInterrupt:
        print(f"\n\033[0;37m[\033[0;33m-\033[0;37m] Ctrl+C pressed. EXITING.")
        sys.exit(1)
    except requests.RequestException as reqexc:
        print(f"\033[0;37m[\033[0;33m-\033[0;37m] An error was defined!\n{reqexc}")
        sys.exit(1)
    except Exception as error:
        print(f"\033[0;37m[\033[0;33m-\033[0;37m] An error was defined!\n{error}")
        sys.exit(1)

    tend = datetime.now()

    print(
        f"\033[0;33m=\033[0;37m" * 50,
        f"\n \033[0;37m[\033[0;31m+\033[0;37m] Hatake done in {tend - tstart}"
    )


def hatake(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:ph", ["addr=", "pipa", "help"])
    except getopt.GetoptError:
        print(
            f" \033[0;37m[\033[0;31m*\033[0;37m] Usage\033[0;31m:\033[0;37m python3 ",
            "hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mh"
        )
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            help_func()
            sys.exit(0)
        elif opt in ("-a", "--addr"):
            ipver4 = arg

            if len(ipver4) == 0:
                print(
                    f" \033[0;37m[\033[0;31m*\033[0;37m] Usage\033[0;31m:\033[0;37m",
                    " python3 hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mh"
                )
                sys.exit(1)

            api_request(ipver4)
        elif opt in ("-p", "--pipa"):
            public_ipv4_request()
            sys.exit(0)
        else:
            raise getopt.GetoptError(
                f" \033[0;37m[\033[0;31m*\033[0;37m] Usage\033[0;31m:\033[0;37m python3 ",
                "hatake\033[0;31m.\033[0;37mpy \033[0;31m-\033[0;37mh")


if __name__ == "__main__":
    print(
        colored(
            pyfiglet.figlet_format(
                "hatake",
                font='bulbhead'
            ), "red"
        ),
        f"\n \033[0;37m[\033[0;31m*\033[0;37m] IPv4\033[0;31m-\033[0;37mLocator",
        " \033[0;31m|\033[0;37m Ver\033[0;31m.:\033[0;37m1\033[0;31m.\033[0;37m0\033[0;31m.\033[0;37m0"
    )

    hatake(sys.argv[1:])
