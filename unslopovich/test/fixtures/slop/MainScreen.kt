package com.example

val Purple80 = Color(0xFFD0BCFF)

@Composable
fun MainScreen(items: List<Item>) {
    Column(modifier = Modifier.verticalScroll(rememberScrollState())) {
        items.forEach { item ->
            Card {
                Card { Text(item.name) }
            }
        }
        Box(Modifier.size(8.dp).background(Color.Green, CircleShape))
        Icon(Icons.Default.Menu, contentDescription = null)
    }
}

class MainActivity : ComponentActivity() {
    override fun onBackPressed() { finish() }
}
