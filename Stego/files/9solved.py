s = '.---- ----- --... / ..... -.... / .---- ..--- ----- / ....- ---.. / .---- .---- ----. / ..... ...-- / ----. ---.. / ----. ---.. / .---- .---- --... / .---- .---- ...--'
# above is morse code

# after decode
d = '107 56 120 48 119 53 98 98 117 113'
e = (107,56,120,48,119,53,98,98,117,113)

password = ''
for i in e :
	password += chr(i)

print password