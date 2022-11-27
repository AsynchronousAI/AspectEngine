import React, { Component } from 'react';
import fs from 'fs';
import { App, AppRegistry, Window, TextInput, View, Text, Button } from 'proton-native';

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
          </View>
        </Window>
      </App>
    );
  }
}

AppRegistry.registerComponent('aspect', <AspectEngine />);