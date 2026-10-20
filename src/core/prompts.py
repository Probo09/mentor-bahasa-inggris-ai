import src.core.env as env

from pathlib import Path

from functools import lru_cache
#from supabase import Client, create_client


@lru_cache
def load_instruction(name: str):
    """Baca file instruksi berdasarkan nama file, contoh: load_instruction('agent-lead')"""

    # Akan otomatis mencari ke: src/agents/instructions/nama_file.md
    path = env.INSTRUCTIONS_DIR / f"{name}.md"  # src/agents/instructions/agent-lead.md

    if not path.exists():
        raise FileNotFoundError(
            f"File instruksi tidak ditemukan: {path}. \n"
            f"Cek nama file di {env.INSTRUCTIONS_DIR}"
        )  # agent-lead, agent-led

    return path.read_text(encoding="utf-8")
