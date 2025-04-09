import { StatusBar } from 'expo-status-bar';
import AntDesign from '@expo/vector-icons/AntDesign';
import { StyleSheet, Text, View, Image } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      {/* Post do feed */}
      <View style={styles.postContainer}>
        {/* Cabeçalho do post com foto de perfil e nome */}
        <View style={styles.header}>
          <Image
            style={styles.profilePic}
            source={{ uri: 'https://randomuser.me/api/portraits/men/1.jpg' }}
          />
          <Text style={styles.username}>jhonathan_ng</Text>
        </View>

        {/* Foto do post */}
        <Image
          style={styles.postImage}
          source={{ uri: 'https://picsum.photos/400/400' }}
        />

        {/* Ícone de like embaixo da foto */}
        <View style={styles.actions}>
          <AntDesign name="hearto" size={24} color="black" />
        </View>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  postContainer: {
    width: '100%',
    marginTop: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10,
  },
  profilePic: {
    width: 40,
    height: 40,
    borderRadius: 20, // Faz a imagem ficar redonda
    marginRight: 10,
  },
  username: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  postImage: {
    width: '100%',
    height: 400,
  },
  actions: {
    padding: 10,
  },
});



import { StatusBar } from 'expo-status-bar';
import AntDesign from '@expo/vector-icons/AntDesign';
import { StyleSheet, Text, View, Image, FlatList } from 'react-native';

// Dados fictícios para simular posts (como se viesse do GitHub)
const POSTS = [
  {
    id: '1',
    username: 'jhonathan_dev',
    profilePic: 'https://randomuser.me/api/portraits/men/1.jpg',
    postImage: 'https://picsum.photos/400/400?random=1',
  },
  {
    id: '2',
    username: 'maria_codes',
    profilePic: 'https://randomuser.me/api/portraits/women/2.jpg',
    postImage: 'https://picsum.photos/400/400?random=2',
  },
];

// Componente para cada post individual
const PostItem = ({ username, profilePic, postImage }) => {
  return (
    <View style={styles.postContainer}>
      {/* Cabeçalho do post com foto de perfil e nome */}
      <View style={styles.header}>
        <Image 
          source={{ uri: profilePic }} 
          style={styles.profilePic} 
        />
        <Text style={styles.username}>{username}</Text>
      </View>

      {/* Imagem do post */}
      <Image 
        source={{ uri: postImage }} 
        style={styles.postImage} 
      />

      {/* Ícone abaixo da foto */}
      <View style={styles.footer}>
        <AntDesign name="heart" size={24} color="black" />
      </View>
    </View>
  );
};

export default function App() {
  return (
    <View style={styles.container}>
      {/* Lista de posts usando FlatList */}
      <FlatList
        data={POSTS}
        renderItem={({ item }) => (
          <PostItem
            username={item.username}
            profilePic={item.profilePic}
            postImage={item.postImage}
          />
        )}
        keyExtractor={item => item.id}
      />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  postContainer: {
    marginBottom: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10,
  },
  profilePic: {
    width: 40,
    height: 40,
    borderRadius: 20, // Faz a foto ficar redonda
    marginRight: 10,
  },
  username: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  postImage: {
    width: '100%',
    height: 300,
  },
  footer: {
    padding: 10,
  },
});




import { StatusBar } from 'expo-status-bar';
import AntDesign from '@expo/vector-icons/AntDesign';
import { StyleSheet, Text, View, Image, FlatList } from 'react-native';

// Dados simulados para o feed (como se fosse do GitHub ou outra fonte)
const feedData = [
  {
    id: '1',
    username: 'jhonathan_ng',
    profilePic: 'https://randomuser.me/api/portraits/men/1.jpg', // Foto de perfil fictícia
    postImage: 'https://picsum.photos/500/500?random=1', // Foto do post fictícia
  },
  {
    id: '2',
    username: 'maria_silva',
    profilePic: 'https://randomuser.me/api/portraits/women/2.jpg',
    postImage: 'https://picsum.photos/500/500?random=2',
  },
];

// Componente principal do App
export default function App() {
  // Função para renderizar cada item do feed
  const renderItem = ({ item }) => (
    <View style={styles.postContainer}>
      {/* Cabeçalho do post: foto de perfil e nome */}
      <View style={styles.header}>
        <Image
          source={{ uri: item.profilePic }}
          style={styles.profilePic}
        />
        <Text style={styles.username}>{item.username}</Text>
      </View>
      {/* Foto do post */}
      <Image
        source={{ uri: item.postImage }}
        style={styles.postImage}
      />
      {/* Ícone abaixo da foto */}
      <View style={styles.iconContainer}>
        <AntDesign name="heart" size={24} color="black" />
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={feedData}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
      <StatusBar style="auto" />
    </View>
  );
}

// Estilos
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  postContainer: {
    marginVertical: 10,
    width: '100%',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10,
  },
  profilePic: {
    width: 40,
    height: 40,
    borderRadius: 20, // Torna a foto redonda
    marginRight: 10,
  },
  username: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  postImage: {
    width: '100%',
    height: 300, // Altura fixa para a foto do post
  },
  iconContainer: {
    padding: 10,
    flexDirection: 'row',
  },
});