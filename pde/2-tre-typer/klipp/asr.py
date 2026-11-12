import sys, sherpa_onnx, soundfile as sf
M='/home/claude/work/asr/sherpa-onnx-whisper-turbo/'
l,_=sf.read('lyd16k.wav',dtype='float32')
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'turbo-encoder.int8.onnx',decoder=M+'turbo-decoder.int8.onnx',tokens=M+'turbo-tokens.txt',language='no',task='transcribe',num_threads=2,tail_paddings=400)
for arg in sys.argv[1:]:
    a,b=map(float,arg.split('-'))
    st=rec.create_stream(); st.accept_waveform(16000,l[int(a*16000):int(b*16000)]); rec.decode_stream(st)
    print(arg,':',st.result.text.strip(),flush=True)
