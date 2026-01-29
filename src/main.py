import qrcode
import argparse

def main():
    # this line was written by a human
    parser = argparse.ArgumentParser(description='Generate a QR code')
    parser.add_argument(
        '--data',
        default='https://google.com',
        help='URL or data to encode (default: https://google.com)'
    )
    parser.add_argument(
        '--ecc',
        choices=['L', 'M', 'Q', 'H'],
        default='H',
        help='Error correction level: L (7%%), M (15%%), Q (25%%), H (30%%) (default: H)'
    )
    parser.add_argument(
        '--output',
        default='qrcode.png',
        help='Output filename (default: qrcode.png)'
    )
    parser.add_argument(
        '--fill-color',
        default='black',
        help='Fill/foreground color (default: black)'
    )
    parser.add_argument(
        '--back-color',
        default='white',
        help='Background color (default: white)'
    )
    args = parser.parse_args()
    
    ecc_map = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H,
    }
    
    # this one too!
    qr = qrcode.QRCode(error_correction=ecc_map[args.ecc])
    qr.add_data(args.data)
    qr.make()
    
    img = qr.make_image(fill_color=args.fill_color, back_color=args.back_color)
    img.save(args.output)
    print(f'QR code generated with ECC level {args.ecc} and saved to {args.output}')

if __name__ == '__main__':
    main()
