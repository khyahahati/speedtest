import speedtest

def get_speed_results():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # bits to megabits
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    # Return a dictionary with rounded values
    return {
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
        "ping": round(ping, 2)
    }

def test_speed():
    results = get_speed_results()
    print(f"Download Speed: {results['download']} Mbps")
    print(f"Upload Speed: {results['upload']} Mbps")
    print(f"Ping: {results['ping']} ms")

if __name__ == "__main__":
    print("Running Internet Speed Test...")
    test_speed()
