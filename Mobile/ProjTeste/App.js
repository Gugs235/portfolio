import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Image } from 'react-native';
import AntDesign from '@expo/vector-icons/AntDesign';

function MinhasCredenciais({ githubUser }) {
  return (
    <View style={styles.credenciaisContainer}>
      <View style={{ flexDirection: 'row', padding: 15, alignItems: 'center' }}>
        <Image
          style={{
            marginRight: 14,
            width: 40,
            height: 40,
            borderRadius: 20,
          }}
          source={{
            uri: `https://github.com/${githubUser}.png`,
          }}
        />
        <View>
          <AntDesign name="hearto" size={24} color="black" />
        </View>
      </View>
    </View>
  );
}

export default function App() {
  return (
    <View style={styles.container}>
      {[
        'WRK7',
        'mauriiicio',
        'anneprimonn',
        'joaovitor9991'

      ].map((githubUser) => (
        <MinhasCredenciais key={githubUser} githubUser={githubUser} />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f2f2f2',
  },
  credenciaisContainer: {
    marginBottom: 20,
  },
  text: {
    color: '#fff',
    marginRight: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
});