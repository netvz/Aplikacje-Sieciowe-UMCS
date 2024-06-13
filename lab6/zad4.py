# telnet dsmka.wintertoad.xyz 587
# Trying 138.2.147.71...
# Connected to dsmka.wintertoad.xyz.
# Escape character is '^]'.
# 220 dsmka.wintertoad.xyz ESMTP
# EHLO fedora
# 250-dsmka.wintertoad.xyz
# 250-PIPELINING
# 250-SIZE 10240000
# 250-ETRN
# 250-AUTH PLAIN LOGIN
# 250-AUTH=PLAIN LOGIN
# 250-ENHANCEDSTATUSCODES
# 250-8BITMIME
# 250-DSN
# 250 CHUNKING
# AUTH LOGIN
# 334 VXNlcm5hbWU6
# dGVzdDFAd2ludGVydG9hZC54eXo=
# 334 UGFzc3dvcmQ6
# UEBzc3cwcmQ=
# 235 2.7.0 Authentication successful
# MAIL FROM: <test1@wintertoad.xyz>
# 250 2.1.0 Ok
# RCPT TO: <test2@wintertoad.xyz>
# 250 2.1.5 Ok
# DATA
# 354 End data with <CR><LF>.<CR><LF>
# From: test1 <test1@wintertoad.xyz>
# To: test2 <test2@wintertoad.xyz>
# Subject: mail z zalacznikiem
# MIME-Version: 1.0
# Content-Type: multipart/mixed; boundary=sep
# --sep
# Tresc
# wiadomosci
# --sep
# Content-Type: text/plain; name=\"plik_tekstowy.txt\"
# Content-Disposition: attachment; filename=\"plik_tekstowy.txt\"
# Content-Transfer-Encoding: base64
# emFrb2Rvd2FuYSB3aWFkb21vc2MgcGxpa3UgCg==
# --sep--  
# .
# 250 2.0.0 Ok: queued as 79F7F10EBE1
# QUIT
# 221 2.0.0 Bye
# Connection closed by foreign host.
