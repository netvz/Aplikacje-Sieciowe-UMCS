# telnet dsmka.wintertoad.xyz 143
# Trying 138.2.147.71...
# Connected to dsmka.wintertoad.xyz.
# Escape character is '^]'.
# * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN AUTH=LOGIN] Dovecot (Debian) ready.
# A1 LOGIN
# A1 BAD Error in IMAP command received by server.
# LOGIN
# LOGIN BAD Error in IMAP command received by server.
# A1 LOGIN test1@wintertoad.xyz P@ssw0rd
# A1 OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY STATUS=SIZE SAVEDATE LITERAL+ NOTIFY SPECIAL-USE QUOTA] Logged in
# A2 LIST "" *
# * LIST (\HasNoChildren \UnMarked \Sent) "." Sent
# * LIST (\HasNoChildren \UnMarked \Trash) "." Trash
# * LIST (\HasNoChildren \UnMarked \Junk) "." Junk
# * LIST (\HasNoChildren \UnMarked \Drafts) "." Drafts
# * LIST (\HasNoChildren) "." INBOX
# A2 OK List completed (0.005 + 0.000 + 0.005 secs).
# A3 STATUS INBOX (MESSAGES)
# * STATUS INBOX (MESSAGES 4)
# A3 OK Status completed (0.003 + 0.000 + 0.002 secs).
# A4 SELECT INBOX
# * FLAGS (\Answered \Flagged \Deleted \Seen \Draft Deleted)
# * OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft Deleted \*)] Flags permitted.
# * 4 EXISTS
# * 0 RECENT
# * OK [UIDVALIDITY 1712573216] UIDs valid
# * OK [UIDNEXT 9] Predicted next UID
# A4 OK [READ-WRITE] Select completed (0.001 + 0.000 secs).
# A5 FETCH 1 BODY[]
# * 1 FETCH (BODY[] {1053}
# Return-Path: <test1@wintertoad.xyz>
# Received: from dsmka.wintertoad.xyz
# 	by dsmka.wintertoad.xyz with LMTP
# 	id N7vxIDcKHWZTZhAABiRgGA
# 	(envelope-from <test1@wintertoad.xyz>); Mon, 15 Apr 2024 11:06:31 +0000
# Received: from michal (unknown [212.182.27.116])
# 	(Authenticated sender: test1@wintertoad.xyz)
# 	by dsmka.wintertoad.xyz (Postfix) with ESMTPA id D14F210EBF8;
# 	Mon, 15 Apr 2024 11:05:26 +0000 (UTC)
# DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=wintertoad.xyz;
# 	s=mail; t=1713179191;
# 	bh=AUJWOaUUN+rC01HB+11HbIwN1IBJ3XOB+SYuRsJ70yY=; h=From:To:Subject;
# 	b=UxB/5UuE0VoLi22NosT2NDst/jJcXFOirLF0GjIwbSASRNUcBDA1Jt5eknvTM8OTZ
# 	 ZI8kydhsgrcJUR9AvfIRMH/KI3PWlUXQ80WCPteS3PFcjMuoT2juzSH10OiqIhZG4V
# 	 8kYLWWvLt7XCE1jVbuxS9dHW3VM5YF0fgrn7AbUXShKtPHOMyVSbzKfSBfKXH2yI6a
# 	 9YzcGLj1qnpjoVviYvbG35o+QmHUWgmqI4qMYsi8GoykQrA8IVTmpEA+qMgr1cM7oI
# 	 ClotNtq/rIhzh1GlkT5bxvjqvE5+uMlf4lpdJusSp5f7noIsosqmG63QlJouLbQY1g
# 	 ZqwHS5t4YIzYw==
# From: test1@wintertoad.xyz
# To: test2@wintertoad.xyz, test1@wintertoad.xyz
# Subject: Tessst

# TREEEESC
# )
# A5 OK Fetch completed (0.004 + 0.000 + 0.003 secs).
# A6 STORE 1 +FLAGS \Seen
# A6 OK Store completed (0.001 + 0.000 secs).
# A7 LOGOUT
# * BYE Logging out
# A7 OK Logout completed (0.001 + 0.000 secs).
# Connection closed by foreign host.
