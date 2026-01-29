import qrcode
import argparse

def main():
    # this line was written by a human
    parser = argparse.ArgumentParser(description='Generate a QR code for google.com')
    parser.add_argument(
        '--ecc',
        choices=['L', 'M', 'Q', 'H'],
        default='H',
        help='Error correction level: L (7%%), M (15%%), Q (25%%), H (30%%) (default: H)'
    )
    args = parser.parse_args()
    
    ecc_map = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H,
    }
    
    # this one too
    qr = qrcode.QRCode(error_correction=ecc_map[args.ecc])
    qr.add_data('https://google.com')
    qr.make()
    
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qrcode.png')
    print(f'QR code generated with ECC level {args.ecc} and saved to qrcode.png')

if __name__ == '__main__':
    main()
