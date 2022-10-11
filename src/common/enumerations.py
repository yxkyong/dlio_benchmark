"""
 Copyright (C) 2020  Argonne, Hariharan Devarajan <hdevarajan@anl.gov>
 This file is part of DLProfile
 DLIO is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
 published by the Free Software Foundation, either version 3 of the published by the Free Software Foundation, either
 version 3 of the License, or (at your option) any later version.
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
 warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 details.
 You should have received a copy of the GNU General Public License along with this program.
 If not, see <http://www.gnu.org/licenses/>.
"""

from enum import Enum

class FrameworkType(Enum):
    """
    Different Computation Type for training loop.
    """
    TENSORFLOW = 'tensorflow'
    PYTORCH = 'pytorch'

    def __str__(self):
        return self.value

class ComputationType(Enum):
    """
    Different Computation Type for training loop.
    """
    NONE = 'none'
    SYNC = 'sync'
    ASYNC = 'async'


class FormatType(Enum):
    """
    Format Type supported by the benchmark.
    """
    TFRECORD = 'tfrecord'
    HDF5 = 'hdf5'
    CSV = 'csv'
    NPZ = 'npz'
    HDF5_OPT = 'hdf5_opt'
    DATA_LOADER = 'data_loader'

    def __str__(self):
        return self.value


class Profiler(Enum):
    """
    Profiler types supported by the benchmark.
    """
    NONE = 'none'
    DARSHAN = 'darshan'
    TENSORBOARD = 'tensorboard'

    def __str__(self):
        return self.value

class Shuffle(Enum):
    """
    Shuffle mode for files and memory.
    """
    OFF = 'off'
    SEED = 'seed'
    RANDOM = 'random'

    def __str__(self):
        return self.value

class ReadType(Enum):
    """
    Type of read to be performed in the benchmark. 
    - On Demand: loading data in a batch-by-batch fashion
    - In Memory: loading data all at once in the beginning. 
    """
    IN_MEMORY = 'memory'
    ON_DEMAND = 'on_demand'

    def __str__(self):
        return self.value

class FileAccess(Enum):
    """
    File access mode.
    - Multi = save dataset into multiple files
    - Shared = save everything in a single file
    - Collective = specific for the shared case, when we want to do collective I/O. 
    “Collective” is MPI specific; typically used for a huge file with small objects; 
    one thread T reads from disk and the other threads read from T's memory, which is used as a cache.
    "
    """
    MULTI = 'multi'
    SHARED = 'shared'
    COLLECTIVE = 'collective'

    def __str__(self):
        return self.value


class Compression(Enum):
    """
    Different Compression Libraries.
    """
    NONE = 'none'
    GZIP = 'gzip'
    LZF = 'lzf'
    BZIP2 = 'bz2'
    ZIP = 'zip'
    XZ = 'xz'

    def __str__(self):
        return self.value
