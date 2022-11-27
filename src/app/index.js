import React, { Component } from 'react';
import fs from 'fs';
import { App, AppRegistry, Window, TextInput, View, Text, Button } from 'proton-native';

const Button = styled.button`
  background-color: black;
  color: white;
  font-size: 20px;
  padding: 10px 60px;
  border-radius: 5px;
  margin: 10px 0px;
  cursor: pointer;
`;

function sayHello(){
  prompt("Button clicked!")
}

class AspectEngine extends Component {
  state = { text: '' };

  shouldComponentUpdate(nextProps, nextState) {
    if (typeof nextState.text === 'string') return false;
    // nextState is set from input
    else return true; // nextState is set from file
  }

  render() {
    return (
      <App>
        <Window>
          <View style={{ flex: 1 }}>
            <Text> Hello World </Text>

            
            <Button onClick={sayHello}>
                    Disabled Button
            </Button>
          </View>
        </Window>
      </App>
    );
  }
}

AppRegistry.registerComponent('aspect', <AspectEngine />);