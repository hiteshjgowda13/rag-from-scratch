# this is embedd class i hav followed embedding bcs i wrote chunking 
from dataclasses import dataclass
from chunking.chunking import Chunk
import numpy as np
@dataclass
class EmbeddedChunk:
    chunk:Chunk
    embedding:np.ndarray