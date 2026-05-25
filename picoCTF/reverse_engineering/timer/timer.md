# Timer
## Description
You will find the flag after analysing this apk Download here.

### Hints
1. Decompile
2. mobsf or jadx

## Solution
Starting by downloading file and it turns out its an apk file so uncompressing the file using `apktool d timer.apk` and got a directory after entering the timer directory;
```
AndroidManifest.xml  apktool.yml  kotlin  original  res  smali  smali_classes2  smali_classes3
```
checking directories 1 by 1, after a little bit time of searching in the second file `apktool.yml`
```
-------Omitted Output-------
usesFramework:
  ids:
  - 1
  tag: null
version: 2.7.0-dirty
versionInfo:
  versionCode: '1'
  versionName: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
```

PWNED!