from pyngrok import ngrok
import re



def open_server_ngrok(puerto, protocol):
        ngrok_tunnel = ngrok.connect(puerto, protocol)
        url = ngrok_tunnel.public_url
        domain = url.replace('tcp://', '')
        puerto = re.search(":(\d+)", url).group(1)
        return domain, puerto
    



