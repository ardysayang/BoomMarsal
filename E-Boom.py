# ! / usr / bin / python
# E-bomber
# Kode ini hanya untuk tujuan pendidikan.
# Gunakan dengan risiko Anda sendiri !!!

impor os
impor smtplib
import passpass
impor sys

server =  raw_input ( ' MailServer Gmail / Yahoo: ' )
pengguna =  raw_input ( ' Email: ' )
passwd = getpass.getpass ( ' Kata Sandi: ' )

to =  raw_input ( ' \ n Ke: ' )
subjectA =  raw_input ( ' Subjek: ' )
body =  raw_input ( ' Pesan: ' )
total =  input ( ' Jumlah kirim: ' )

jika server ==  ' gmail ' :
    smtp_server =  ' smtp.gmail.com '
    port =  587
server elif ==  ' yahoo ' :
    smtp_server =  ' smtp.mail.yahoo.com '
    port =  25
lain :
    print  ' Berlaku hanya untuk gmail dan yahoo. '
    sys.exit ()

cetak  ' '

coba :
    server = smtplib.SMTP (smtp_server, port)
    server.ehlo ()
    if smtp_server ==  " smtp.gmail.com " :
            server.starttls ()
    server.login (pengguna, sandi sandi)
    untuk saya dalam  kisaran ( 1 , total + 1 ):
        subjectB = os.urandom ( 5 )
	subject = subjectA +  "  "  + subjectB
        msg =  ' Dari: '  + pengguna +  ' \ n Subjek: '  + subjek +  ' \ n '  + badan
        server.sendmail (pengguna, ke, msg)
        print  " \ r E-mail yang dikirim: % i "  % i
        sys.stdout.flush ()
    server.quit ()
    cetak  ' \ n Selesai !!! '
kecuali  KeyboardInterrupt :
    print  ' [-] Dibatalkan '
    sys.exit ()
kecuali smtplib.SMTPAuthenticationError:
    print  ' \ n [!] Nama pengguna atau kata sandi yang Anda masukkan salah. '
    sys.exit ()