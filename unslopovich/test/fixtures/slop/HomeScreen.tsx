import { ScrollView, View, Text, TextInput, Pressable } from "react-native";
import { LinearGradient } from "expo-linear-gradient";
import MaskedView from "@react-native-masked-view/masked-view";
import { createDrawerNavigator } from "@react-navigation/drawer";

export function HomeScreen({ items }) {
  return (
    <ScrollView>
      <LinearGradient colors={["#7C3AED", "#EC4899"]} style={{ padding: 24 }}>
        <Text>Welcome back!</Text>
        <Text>Unlock your potential with seamless planning ✨</Text>
      </LinearGradient>
      <MaskedView maskElement={<Text>Pro</Text>} />
      <Card>
        <Card>
          <Text>12.5k</Text>
          <Text>+23%</Text>
        </Card>
      </Card>
      <View style={{ width: 8, height: 8, borderRadius: 4, backgroundColor: "green" }} />
      <View className="h-2 w-2 rounded-full bg-emerald-500" />
      <Text allowFontScaling={false}>🚀 Fast</Text>
      <TextInput placeholder="Search" />
      {items.map((item) => (
        <Text key={item.id}>{item.name}</Text>
      ))}
      <Text>Oops! Something went wrong</Text>
      <Button title="Submit" />
      <View style={{ shadowColor: "#8B5CF6", shadowRadius: 20 }} onHoverIn={() => {}} />
    </ScrollView>
  );
}

export const screenOptions = { gestureEnabled: false };
