# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'recon_all', 'flirt', 'reorient2std', 'fsldwipreproc']

# %% ../00_core.ipynb 4
def foo(): pass

# %% ../00_core.ipynb 6
def recon_all(image_fname,
           subject_name,
           parallel=True,
           openmp=4,
           subjects_dir=None,
           license_fname=None):
    "Generate call to the main FreeSurfer script `recon-all` on a given image."
    import os, subprocess
    env = {}
    if subjects_dir is not None:
        env['SUBJECTS_DIR'] = subjects_dir
    argv = [
        'recon-all', '-s', subject_name, '-i', image_fname
    ]
    if parallel:
        argv.append('-parallel')
    if openmp:
        argv.extend(['-openmp', str(openmp)])
    return argv, env

# %% ../00_core.ipynb 8
def flirt(): "Register images."

def reorient2std(): "Standardize image data layout."

# %% ../00_core.ipynb 10
def fsldwipreproc(): "Preprocess a DWI image."
