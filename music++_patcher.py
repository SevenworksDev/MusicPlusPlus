import os, shutil
from colorama import just_fix_windows_console
just_fix_windows_console()

banner = '''
\033[95m ::::    ::::  :::    :::  :::::::: ::::::::::: ::::::::                             
\033[95m +:+:+: :+:+:+ :+:    :+: :+:    :+:    :+:    :+:    :+:     :+:           :+:      
\033[95m +:+ +:+:+ +:+ +:+    +:+ +:+           +:+    +:+            +:+           +:+      
\033[95m +#+  +:+  +#+ +#+    +:+ +#++:++#++    +#+    +#+       +#++:++#++:++ +#++:++#++:++ 
\033[95m +#+       +#+ +#+    +#+        +#+    +#+    +#+            +#+           +#+      
\033[95m #+#       #+# #+#    #+# #+#    #+#    #+#    #+#    #+#     #+#           #+#      
\033[95m ###       ###  ########   ######## ########### ########                             

\033[95m :::::::::     ::: ::::::::::: :::    :::  ::::::::  :::::::::: :::::::::            
\033[95m :+:    :+:  :+: :+:   :+:     :+:    :+: :+:    :+: :+:        :+:    :+:           
\033[95m +:+    +:+ +:+   +:+  +:+     +:+    +:+ +:+        +:+        +:+    +:+           
\033[95m +#++:++#+ +#++:++#++: +#+     +#++:++#++ +#+        +#++:++#   +#++:++#:            
\033[95m +#+       +#+     +#+ +#+     +#+    +#+ +#+        +#+        +#+    +#+           
\033[95m #+#       #+#     #+# #+#     #+#    #+# #+#    #+# #+#        #+#    #+#           
\033[95m ###       ###     ### ###     ###    ###  ########  ########## ###    ###           
'''
print(banner)

print('\033[92m [0%] Reading GeometryDash.exe')
with open('GeometryDash.exe', 'rb') as f:
    gd = f.read()
print('\033[92m [25%] Replacing links in GeometryDash.exe')
gd = gd.replace(b'https://www.boomlings.com/database/getGJSongInfo.php', b'http://music.sevenworks.eu.org/req/getGJSongInfo.php')
gd = gd.replace(b'https://www.boomlings.com/database/getCustomContentURL.php', b'http://music.sevenworks.eu.org/req/getCustomContentURL.php')
print('\033[92m [50%] Copying modified GeometryDash.exe to Music++.exe')
with open('Music++.exe', 'wb') as f:
    f.write(gd)
print('\033[92m [75%] Patched GeometryDash.exe')
os.makedirs(os.path.join(os.getenv('LOCALAPPDATA'), 'Music++'), exist_ok=True)
shutil.copy(os.path.join(os.getenv('LOCALAPPDATA'), 'GeometryDash', 'CCGameManager.dat'), os.path.join(os.getenv('LOCALAPPDATA'), 'Music++', 'CCGameManager.dat'))
shutil.copy(os.path.join(os.getenv('LOCALAPPDATA'), 'GeometryDash', 'CCLocalLevels.dat'), os.path.join(os.getenv('LOCALAPPDATA'), 'Music++', 'CCLocalLevels.dat'))
input('\033[92m [100%] Copied save data to Music++ LocalAppData folder, have fun :)')