# # import asyncio
# # import sounddevice as sd
# # import numpy as np
# # from deepgram import DeepgramClient
# # from deepgram.core.events import EventType

# # DEEPGRAM_API_KEY = "958fe5b0855210467897796000ed735359a24ae9"
# # SAMPLE_RATE      = 16000

# # async def run():
# #     client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

# #     async with client.listen.v2.connect(
# #         model="nova-3",
# #         encoding="linear16",
# #         sample_rate=SAMPLE_RATE
# #     ) as connection:

# #         connection.on(EventType.OPEN,   lambda _: print("✅ Connection opened"))
# #         connection.on(EventType.MESSAGE, lambda msg: handle_message(msg))
# #         connection.on(EventType.CLOSE,  lambda _: print("❌ Connection closed"))
# #         connection.on(EventType.ERROR,  lambda err: print("⚠️ Error:", err))

# #         def callback(indata, frames, time, status):
# #             if status:
# #                 print("Status:", status)
# #             connection.send(indata.tobytes())

# #         print("🎙️ Listening... Press Ctrl+C to stop")
# #         with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype=np.int16, callback=callback):
# #             await connection.start_listening()

# # def handle_message(msg):
# #     try:
# #         transcript = msg.channel.alternatives[0].transcript
# #         if transcript:
# #             print("🗣️", transcript)
# #     except Exception:
# #         pass

# # if __name__ == "__main__":
# #     asyncio.run(run())

# import asyncio
# import numpy as np
# import sounddevice as sd
# from deepgram import DeepgramClient, DeepgramClientOptions, LiveTranscriptionOptions
# from deepgram import LiveTranscriptionEvent

# DEEPGRAM_API_KEY = "YOUR_DEEPGRAM_API_KEY"
# SAMPLE_RATE = 16000

# async def main():
#     # Initialize Deepgram client
#     config = DeepgramClientOptions(
#         verbose=False
#     )
#     deepgram = DeepgramClient(DEEPGRAM_API_KEY, config)

#     # Create a live transcription connection
#     dg_connection = deepgram.listen.live.v("1")

#     # Define event handlers
#     @dg_connection.on(LiveTranscriptionEvent.OPEN)
#     async def on_open(connection, event):
#         print("✅ Connected to Deepgram — start speaking!")

#     @dg_connection.on(LiveTranscriptionEvent.TRANSCRIPT_RECEIVED)
#     async def on_transcript(connection, result):
#         transcript = result.channel.alternatives[0].transcript
#         if transcript:
#             print("🗣️", transcript)

#     @dg_connection.on(LiveTranscriptionEvent.CLOSE)
#     async def on_close(connection, event):
#         print("❌ Connection closed.")

#     @dg_connection.on(LiveTranscriptionEvent.ERROR)
#     async def on_error(connection, event):
#         print("⚠️ Error:", event)

#     # Configure live options
#     options = LiveTranscriptionOptions(
#         model="nova-2",
#         encoding="linear16",
#         sample_rate=SAMPLE_RATE,
#         channels=1,
#         interim_results=True
#     )

#     # Start streaming
#     await dg_connection.start(options)

#     # Stream microphone audio to Deepgram
#     def callback(indata, frames, time, status):
#         if status:
#             print(status)
#         dg_connection.send(indata.tobytes())

#     print("🎤 Listening... (Press Ctrl+C to stop)")
#     try:
#         with sd.InputStream(
#             samplerate=SAMPLE_RATE,
#             channels=1,
#             dtype=np.int16,
#             callback=callback
#         ):
#             await asyncio.Future()  # keep running
#     except KeyboardInterrupt:
#         print("🛑 Stopping transcription...")
#     finally:
#         await dg_connection.finish()

# # Run the async loop
# asyncio.run(main())


# import asyncio
# import sounddevice as sd
# from deepgram import DeepgramClient, LiveOptions
# API_KEY = "YOUR_API_KEY"
# SAMPLE_RATE = 16000
# CHANNELS = 1
# BLOCK_SIZE = 8000
# async def main():
# deepgram = DeepgramClient(API_KEY)
# dg_connection = deepgram.listen.websocket.v("1")
# @dg_connection.on('transcript')
# async def on_transcript(self, result, **kwargs):
# transcript = result.channel.alternatives[0].transcript
# if transcript:
# print("􋆶􋆷􋆸􋆹", transcript)
# await dg_connection.start(
# LiveOptions(
# model="nova-2",
# language="en",
# encoding="linear16",
# sample_rate=SAMPLE_RATE,
# punctuate=True
# )
# )
# def callback(indata, frames, time, status):
# if status:
# print("Mic status:", status)
# 47
# dg_connection.send(indata.tobytes())
# print("􈘒􈘐􈘑 Speak now... (Press Ctrl+C to stop)")
# try:
# with sd.InputStream(
# samplerate=SAMPLE_RATE,
# blocksize=BLOCK_SIZE,
# dtype='int16',
# channels=CHANNELS,
# callback=callback
# ):
# await asyncio.Future()
# except KeyboardInterrupt:
# print("\n🛑 Stopping transcription...")
# finally:
# await dg_connection.finish()
# if __name__ == "__main__":
# asyncio.run(main())

# import sounddevice as sd
# import numpy as np
# from deepgram import DeepgramClient
# from deepgram.core.events import EventType

# # 🔑 Replace with your Deepgram API key
# DEEPGRAM_API_KEY = "YOUR_API_KEY"

# # 🎙️ Audio parameters
# SAMPLE_RATE = 16000
# CHANNELS = 1

# def main():
#     # Initialize client
#     dg_client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

#     # Connect to live transcription
#     with dg_client.listen.v2.connect(
#         model="nova-3",            # Latest model for live transcription
#         encoding="linear16",       # PCM 16-bit audio
#         sample_rate=SAMPLE_RATE    # 16kHz sampling rate
#     ) as connection:

#         # ✅ Event handlers
#         connection.on(EventType.OPEN, lambda _: print("✅ Connection opened. Speak now!"))
#         connection.on(EventType.CLOSE, lambda _: print("❌ Connection closed."))
#         connection.on(EventType.ERROR, lambda e: print("⚠️ Error:", e))

#         def on_message(msg):
#             try:
#                 # Extract transcript text
#                 transcript = msg.channel.alternatives[0].transcript
#                 if transcript:
#                     print("🗣️", transcript)
#             except Exception:
#                 pass

#         connection.on(EventType.MESSAGE, on_message)

#         # 🎧 Capture microphone input and stream to Deepgram
#         def callback(indata, frames, time, status):
#             if status:
#                 print("🎤 Mic status:", status)
#             connection.send(indata.tobytes())

#         print("🎙️ Listening... Press Ctrl+C to stop")
#         try:
#             with sd.InputStream(
#                 samplerate=SAMPLE_RATE,
#                 channels=CHANNELS,
#                 dtype='int16',
#                 callback=callback
#             ):
#                 connection.start_listening()
#         except KeyboardInterrupt:
#             print("\n🛑 Stopping transcription...")
#         finally:
#             connection.finish()

# if __name__ == "__main__":
#     main()


# import sounddevice as sd
# import numpy as np
# from deepgram import DeepgramClient
# from deepgram.core.events import EventType

# DEEPGRAM_API_KEY = "958fe5b0855210467897796000ed735359a24ae9"  # Replace this!
# SAMPLE_RATE = 16000
# CHANNELS = 1

# def main():
#     client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

#     # Use supported live model: "general" or "nova-2"
#     with client.listen.v2.connect(
#         model="nova-2",          # use "nova-2" (live model)
#         encoding="linear16",
#         sample_rate=SAMPLE_RATE,
#         interim_results=True 
#     ) as connection:

#         # Event handlers
#         connection.on(EventType.OPEN, lambda _: print("✅ Connection opened. Speak now!"))
#         connection.on(EventType.CLOSE, lambda _: print("❌ Connection closed."))
#         connection.on(EventType.ERROR, lambda e: print("⚠️ Error:", e))

#         def on_message(msg):
#             try:
#                 transcript = msg.channel.alternatives[0].transcript
#                 if transcript:
#                     print("🗣️", transcript)
#             except Exception:
#                 pass

#         connection.on(EventType.MESSAGE, on_message)

#         def callback(indata, frames, time, status):
#             if status:
#                 print("🎤 Mic status:", status)
#             connection.send(indata.tobytes())

#         print("🎙️ Listening... Press Ctrl+C to stop")
#         try:
#             with sd.InputStream(
#                 samplerate=SAMPLE_RATE,
#                 channels=CHANNELS,
#                 dtype='int16',
#                 callback=callback
#             ):
#                 connection.start_listening()
#         except KeyboardInterrupt:
#             print("\n🛑 Stopping transcription...")
#         finally:
#             connection.finish()

# if __name__ == "__main__":
#     main()

import sounddevice as sd
import numpy as np
from deepgram import DeepgramClient
from deepgram.core.events import EventType

# 🔑 Your Deepgram API Key
DEEPGRAM_API_KEY = "958fe5b0855210467897796000ed735359a24ae9"

# 🎙️ Audio config
SAMPLE_RATE = 16000
CHANNELS = 1

def main():
    # Initialize client
    dg = DeepgramClient(api_key=DEEPGRAM_API_KEY)

    # ✅ The current SDK expects parameters wrapped in an "options" dict
    options = {
        "model": "nova-2",          # or "general" if nova-2 not available
        "encoding": "linear16",
        "sample_rate": SAMPLE_RATE,
        "smart_format": True,       # adds punctuation/formatting
        "interim_results": True     # stream partial captions
    }

    # Establish live connection
    with dg.listen.v2.connect(options=options) as connection:

        # Event hooks
        connection.on(EventType.OPEN, lambda _: print("✅ Connected — speak now!"))
        connection.on(EventType.CLOSE, lambda _: print("❌ Connection closed."))
        connection.on(EventType.ERROR, lambda e: print("⚠️ Error:", e))

        def on_message(msg):
            try:
                transcript = msg.channel.alternatives[0].transcript
                if transcript:
                    print("🗣️", transcript)
            except Exception:
                pass

        connection.on(EventType.MESSAGE, on_message)

        # Capture mic and stream
        def callback(indata, frames, time, status):
            if status:
                print("🎤 Mic status:", status)
            connection.send(indata.tobytes())

        print("🎧 Listening... Press Ctrl+C to stop.")
        try:
            with sd.InputStream(
                samplerate=SAMPLE_RATE,
                channels=CHANNELS,
                dtype='int16',
                callback=callback
            ):
                connection.start_listening()
        except KeyboardInterrupt:
            print("\n🛑 Stopping transcription...")
        finally:
            connection.finish()

if __name__ == "__main__":
    main()
