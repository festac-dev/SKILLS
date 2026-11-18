import { FlatList, Text, TextInput, KeyboardAvoidingView, View } from "react-native";

// A purple gradient used to live here: <LinearGradient colors={["#7C3AED"]} />
export function HomeScreen({ items, total }) {
  return (
    <KeyboardAvoidingView behavior="padding">
      <TextInput placeholder="Search zones" />
      <FlatList data={items} renderItem={({ item }) => <Text>{item.name}</Text>} />
      <Text>{total} zones</Text>
      <View style={{ width: "100%", height: 1 }} />
      <Text>Couldn't load zones. Check your connection and pull to retry.</Text>
      <Button title="Add zone" />
      <Text>Visit https://example.com for help</Text>
    </KeyboardAvoidingView>
  );
}
