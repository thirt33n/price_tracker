import json
import websocket
import time

def getPrice():
    symbol = 'btcusdt'
    socket = f'wss://stream.binance.com:9443/ws/{symbol}@avgPrice'

    high_price = None  

    def on_message(ws, message):
        nonlocal high_price  
        try:
            msg = json.loads(message)
            high_price = round(float(msg['w']), 2)
          
            ws.close()      # Closing after 1 fetch since ws keeps producing new values to make it easier to handle later
        except Exception as e:
            print(f"Error processing message: {e}")

    def on_error(ws, error):
        print(f"WebSocket Error: {error}")

    def on_close(ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(ws):
        print("Opened connection")

    ws = websocket.WebSocketApp(socket,
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_error=on_error,
                                  on_close=on_close)

    ws.run_forever()

    return high_price  



