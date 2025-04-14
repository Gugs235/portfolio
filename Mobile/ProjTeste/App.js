import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, ScrollView, Dimensions } from 'react-native';
import AntDesign from '@expo/vector-icons/AntDesign';

// Configura dimensões específicas para o Xiaomi Redmi Note 8 (1080x2340 pixels, densidade ~390 ppi)
const WINDOW_WIDTH = 310; // Largura em dp (1080px / 3, assumindo escala 3x)
const WINDOW_HEIGHT = 780; // Altura em dp (2340px / 3, ajustado para área útil)

function MinhasCredenciais({ githubUser }) {
  return (
    <View style={styles.credenciaisContainer}>
      <View style={styles.userInfo}>
        <Image
          style={styles.profileImage}
          source={{
            uri: `https://github.com/${githubUser}.png`,
          }}
        />
        <Text style={styles.username}>{githubUser}</Text>
      </View>
      <Image
        style={styles.postImage}
        source={{
          uri: `https://github.com/${githubUser}.png`,
        }}
      />
      <View style={styles.heartContainer}>
        <AntDesign name="hearto" size={24} color="black" />
      </View>
    </View>
  );
}

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {[
          'WRK7',
          'mauriiicio',
          'anneprimonn',
          'joaovitor9991',
          'Gugs235',
          'dev-rls',
          'HisanoEdu',
        ].map((githubUser) => (
          <MinhasCredenciais key={githubUser} githubUser={githubUser} />
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f2f2f2',
    width: WINDOW_WIDTH,
    height: WINDOW_HEIGHT,
  },
  scrollContent: {
    paddingTop: 20,
    paddingBottom: 20,
  },
  credenciaisContainer: {
    marginBottom: 20,
    backgroundColor: '#fff',
    borderRadius: 10,
    marginHorizontal: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
    width: WINDOW_WIDTH - 20, // Ajusta para margens
  },
  userInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 15,
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 20,
    marginRight: 10,
  },
  username: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
  },
  postImage: {
    width: '100%',
    height: 300 * (WINDOW_WIDTH - 20) / 360, // Escala proporcionalmente
    resizeMode: 'cover',
  },
  heartContainer: {
    padding: 10,
    alignItems: 'flex-start',
  },
});