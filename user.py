#!/usr/bin/env python3
# Copyright (C) @SakirBey1
# Bu program ücretsiz bir yazılımdır: yeniden dağıtabilir ve/veya değiştirebilirsiniz
# tarafından yayınlanan GNU Affero Genel Kamu Lisansı koşulları altında
# Özgür Yazılım Vakfı, Lisansın 3. sürümü veya
# (isteğe bağlı olarak) herhangi bir sonraki sürüm.

# Bu program faydalı olması ümidiyle dağıtılmaktadır,
# ancak HİÇBİR GARANTİ YOKTUR; zımni garanti bile olmadan
# SATILABİLİRLİK veya BELİRLİ BİR AMACA UYGUNLUK. görmek
# Daha fazla ayrıntı için GNU Affero Genel Kamu Lisansı.

# GNU Affero Genel Kamu Lisansının bir kopyasını almış olmalısınız
# bu programla birlikte. Değilse, bkz. <https://www.gnu.org/licenses/>.
from pytgcalls import PyTgCalls
from pyrogram import Client
from config import Config
from utils import LOGGER

USER = Client(
    Config.SESSION,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="userplugins")
    )
group_call = PyTgCalls(USER, cache_duration=180)


