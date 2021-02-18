var a,b;
Object.assign(global, { WebSocket: require('ws') });

const StompJs = require('@stomp/stompjs/esm5');

process.argv.forEach(function (val, index, array) {
	if(index == 2){
		a = val;
	}
	if(index == 3){
		b = val;
	}
});

let stompClient;
    const stompConfig = {
      // Typically login, passcode and vhost
      // Adjust these for your broker
      connectHeaders: {
        login: "bola",
        passcode: "mrbola01"
      },

      // Broker URL, should start with ws:// or wss:// - adjust for your broker setup
      brokerURL: "ws://134.209.244.238:15674/ws",

      // If disconnected, it will retry after 200ms
      reconnectDelay: 200,

      // Subscriptions should be done inside onConnect as those need to reinstated when the broker reconnects
      onConnect: function (frame) {
		  publishMessage(a,b)
		  process.exit()
      }
    };

    // Create an instance
    stompClient = new StompJs.Client(stompConfig);

    // You can set additional configuration here

    // Attempt to connect
    stompClient.activate();

    function publishMessage(user, message) {
      // trying to publish a message when the broker is not connected will throw an exception
      if (!stompClient.connected) {
        return false;
      }
      if (message.length > 0) {
        const payLoad = { user: user, message: message };

        // You can additionally pass headers
        stompClient.publish({destination: '/topic/chat', body: JSON.stringify(payLoad)});
      }
      return true;
    }