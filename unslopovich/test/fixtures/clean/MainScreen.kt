@Composable
fun MainScreen(items: List<Item>) {
    LazyColumn {
        items(items) { item -> ListItem(headlineContent = { Text(item.name) }) }
    }
    Card { Text("Single card") }
}
