"""Optional Higgsfield CLI adapter boundary.

This module intentionally does not embed Cully Hill Boys prompts, seeds, workflows, references,
or other study-only release materials. It accepts only project-owned structured prompt packets.
"""
from __future__ import annotations
import json, subprocess, shutil
from typing import Dict, Any

class HiggsfieldCLIAdapter:
    def __init__(self,binary='higgsfield'): self.binary=binary
    def available(self): return shutil.which(self.binary) is not None
    def capabilities(self):
        return {'image_generation':True,'video_generation':True,'audio_generation':True,'character_identity':True,'live_schema_required':True}
    def build_command(self,prompt_packet:Dict[str,Any],model:str,output_dir:str):
        # Higgsfield's job-set/model identifier is positional. Live callers must still
        # query `higgsfield model get <id> --json` before constructing model parameters.
        prompt='; '.join(f"{s['field']}: {json.dumps(s['value'],ensure_ascii=False)}" for s in prompt_packet['sections'])
        return [self.binary,'generate','create',model,'--prompt',prompt,'--output-dir',output_dir,'--json']
    def submit(self,prompt_packet:Dict[str,Any],model:str,output_dir:str,dry_run=True,authorized=False):
        cmd=self.build_command(prompt_packet,model,output_dir)
        if dry_run: return {'dry_run':True,'command':cmd,'status':'research_only_legacy_boundary'}
        # v0.2 deliberately disables legacy live execution because this adapter does
        # not yet satisfy the production adapter contract (capability manifest,
        # idempotency, estimate, lifecycle, policy metadata, normalized cost).
        # A real implementation must live behind film_studio_os.adapters.ProviderAdapter.
        raise RuntimeError('legacy Higgsfield CLI live execution disabled; use a production contract adapter after explicit authorization')
