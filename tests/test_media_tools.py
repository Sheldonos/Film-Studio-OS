import shutil,subprocess
from pathlib import Path
import pytest
from film_studio_os.tools.media import frames_to_timecode,probe_media,technical_qc,extract_frame,extract_audio,measure_loudness

def test_timecode_nondrop_and_dropframe():
    assert frames_to_timecode(24*60,24)=='00:01:00:00'
    assert ';' in frames_to_timecode(17982,29.97,True)
    with pytest.raises(ValueError): frames_to_timecode(1,24,True)

@pytest.mark.skipif(not shutil.which('ffmpeg') or not shutil.which('ffprobe'),reason='ffmpeg/ffprobe unavailable')
def test_probe_extract_and_delivery_qc_are_deterministic(tmp_path):
    src=tmp_path/'fixture.mp4'
    cmd=[shutil.which('ffmpeg'),'-nostdin','-v','error','-f','lavfi','-i','color=c=black:s=320x180:r=24:d=1','-f','lavfi','-i','sine=frequency=440:sample_rate=48000:duration=1','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-y',str(src)]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=30); assert r.returncode==0,r.stderr
    p=probe_media(src); assert p['duration_seconds']>0; assert any(s['codec_type']=='video' for s in p['streams'])
    q=technical_qc(src,{'video_required':True,'audio_required':True,'width':320,'height':180,'frame_rate':24}); assert q['passed']
    bad=technical_qc(src,{'video_required':True,'width':1920}); assert not bad['passed']
    frame=extract_frame(tmp_path,'fixture.mp4','derived/frame.png',0.2); assert Path(frame['path']).exists()
    audio=extract_audio(tmp_path,'fixture.mp4','derived/audio.wav'); assert Path(audio['path']).exists()
    loud=measure_loudness(src); assert loud['integrated_lufs'] is not None and loud['true_peak_dbtp'] is not None
