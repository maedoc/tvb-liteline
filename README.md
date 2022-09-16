tvb-liteline
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install tvb_liteline
```

## How to use

Fill me in please! Don’t forget code examples:

``` python
1+1
```

    2

``` python
help(recon_all)
```

    Help on function recon_all in module tvb_liteline.core:

    recon_all(image_fname, subject_name, parallel=True, openmp=4, subjects_dir=None, license_fname=None)
        Generate call to the main FreeSurfer script `recon-all` on a given image.

``` python
' '.join(recon_all('foo', 'bar')[0])
```

    'recon-all -s bar -i foo -parallel -openmp 4'

🎉 that was easy!
