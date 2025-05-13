
async function draw_card_from_deck() {
	const card = eel.draw_card_from_deck()();
	// return JSON.parse(card)
	return await card
}
