import { StyleSheet,Text, View,Image, Button } from 'react-native';

export default function App() {
    const botao_clicado = () => {
      alert("Você clicou no Botão!")
    };



  return (
    <View style={styles.container}>
      <Text>Olá, Mundo!</Text> 
      <Image
        style={styles.Image}
        source={require('./foto/HomemTrabalho.jpg')}
        />
        <Button title='Clique Aqui' onPress={botao_clicado}></Button>
      </View>
    );
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
     // alignItems: 'center',
     // justifyContent: 'center',
    },
  
  });
  