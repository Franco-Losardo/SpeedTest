import speedtest


st = speedtest.Speedtest()
option = input("""Choose below which speed you want to test
1 Download
2 Upload
3 Ping
Option: """)


def sptest():
    if option == 1:
        st.get_best_server()
        print(round(st.download() / 8e+6, 2), "Mb/s")
    elif option == 2:
        st.get_best_server()
        print(round(st.upload() / 8e+6, 2), "Mb/s")
    elif option == 3:
        servernames = []
        st.get_best_server()
        st.get_servers(servernames)
        print(round(st.results.ping), "ms")
    else:
        print("Wrong option, please try again")


sptest()
