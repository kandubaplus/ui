# -*- mode: python -*-

block_cipher = None


a = Analysis(['S.py'],
             pathex=['c:\\Users\\kandu\\source\\repos\\ui\\ui'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['urllib3'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='S',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
