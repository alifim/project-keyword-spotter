from audio_recorder import AudioRecorder

def test():
    recorder = AudioRecorder(
        raw_audio_sample_rate_hz=48000,
        downsample_factor=1,
        device_index=None,
    )

    with recorder:
        while True:
            print("test")


if __name__ == "__main__":
    test()
