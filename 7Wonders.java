import io
import tkinter as tk
from urllib.request import Request, urlopen

from PIL import Image, ImageTk


class Wonders7:
	def displayInformation(self):
		print("The Seven Wonders of the Ancient World:")


class GreatPyramidOfGiza(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Great%20Pyramid%20of%20Giza.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[1] GREAT PYRAMID OF GIZA - EGYPT")
		print("=" * 72)
		print("Purpose: Tomb of Pharaoh Khufu")
		print("Built: Around 2560 BCE during Egypt's Fourth Dynasty")
		print("Materials: Limestone blocks with a polished outer casing")
		print("Importance: The oldest and only surviving ancient wonder")
		print(f"Image: {self.image_url}")


class HangingGardensOfBabylon(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Hanging%20Gardens%20of%20Babylon.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[2] HANGING GARDENS OF BABYLON - MESOPOTAMIA")
		print("=" * 72)
		print("Purpose: A spectacular garden complex built on raised terraces")
		print("Tradition: Often associated with King Nebuchadnezzar II")
		print("Design: Terraces were said to hold trees, flowers, and flowing water")
		print("Historical note: No confirmed archaeological remains have been found")
		print(f"Image: {self.image_url}")


class StatueOfZeusAtOlympia(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Statue%20of%20Zeus.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[3] STATUE OF ZEUS AT OLYMPIA - GREECE")
		print("=" * 72)
		print("Purpose: A religious image honoring Zeus, king of the Greek gods")
		print("Created: Around 430 BCE by the sculptor Phidias")
		print("Materials: Gold and ivory over a wooden framework")
		print("Historical note: It was later moved to Constantinople and destroyed by fire")
		print(f"Image: {self.image_url}")


class TempleOfArtemisAtEphesus(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Temple%20of%20Artemis.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[4] TEMPLE OF ARTEMIS AT EPHESUS - TURKEY")
		print("=" * 72)
		print("Purpose: Sanctuary dedicated to Artemis, goddess of the hunt")
		print("Built: The most famous version was completed around 550 BCE")
		print("Design: A huge marble temple filled with columns and sculptures")
		print("Historical note: It was destroyed and rebuilt several times")
		print(f"Image: {self.image_url}")


class MausoleumAtHalicarnassus(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Mausoleum%20at%20Halicarnassus.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[5] MAUSOLEUM AT HALICARNASSUS - TURKEY")
		print("=" * 72)
		print("Purpose: Monumental tomb for Mausolus, ruler of Caria")
		print("Built: Around 350 BCE by Mausolus's wife and successor Artemisia II")
		print("Design: Combined Greek columns, Egyptian forms, and a stepped roof")
		print("Historical note: Earthquakes eventually reduced the monument to ruins")
		print(f"Image: {self.image_url}")


class ColossusOfRhodes(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Colossus%20of%20Rhodes.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[6] COLOSSUS OF RHODES - GREECE")
		print("=" * 72)
		print("Purpose: A victory monument dedicated to the sun god Helios")
		print("Built: Around 280 BCE after Rhodes survived a long siege")
		print("Materials: Bronze plates supported by an iron framework")
		print("Historical note: An earthquake toppled the statue about 56 years later")
		print(f"Image: {self.image_url}")


class LighthouseOfAlexandria(Wonders7):
	image_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Lighthouse%20of%20Alexandria.jpg"

	def displayInformation(self):
		print("\n" + "=" * 72)
		print("[7] LIGHTHOUSE OF ALEXANDRIA - EGYPT")
		print("=" * 72)
		print("Purpose: Guided ships safely into Alexandria's busy harbor")
		print("Built: During the reigns of Ptolemy I and Ptolemy II")
		print("Design: A tall stone tower with a fire and reflective signal at its summit")
		print("Historical note: Earthquakes damaged it over centuries before its collapse")
		print(f"Image: {self.image_url}")


def display_images(wonders):
	root = tk.Tk()
	root.title("The Seven Wonders - Image Gallery")
	root.geometry("1000x800")

	container = tk.Frame(root, padx=20, pady=20)
	container.pack(fill="both", expand=True)
	canvas = tk.Canvas(container, highlightthickness=0)
	scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
	gallery = tk.Frame(canvas)
	gallery.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
	canvas.create_window((0, 0), window=gallery, anchor="nw")
	canvas.configure(yscrollcommand=scrollbar.set)
	canvas.pack(side="left", fill="both", expand=True)
	scrollbar.pack(side="right", fill="y")

	image_references = []
	for number, wonder in enumerate(wonders, start=1):
		section = tk.LabelFrame(
			gallery,
			text=f"{number}. {wonder.__class__.__name__}",
			font=("Segoe UI", 12, "bold"),
			padx=12,
			pady=12,
		)
		section.pack(fill="x", pady=8)
		try:
			request = Request(wonder.image_url, headers={"User-Agent": "SevenWondersViewer/1.0"})
			with urlopen(request, timeout=20) as response:
				image = Image.open(io.BytesIO(response.read()))
			image.thumbnail((420, 260))
			photo = ImageTk.PhotoImage(image)
			image_references.append(photo)
			tk.Label(section, image=photo).pack()
		except Exception as error:
			tk.Label(section, text=f"Image could not be loaded: {error}").pack()

	root.mainloop()


def main():
	print("=" * 72)
	print("                 THE SEVEN WONDERS OF THE ANCIENT WORLD")
	print("=" * 72)
	wonders = [
		GreatPyramidOfGiza(),
		HangingGardensOfBabylon(),
		StatueOfZeusAtOlympia(),
		TempleOfArtemisAtEphesus(),
		MausoleumAtHalicarnassus(),
		ColossusOfRhodes(),
		LighthouseOfAlexandria(),
	]

	for wonder in wonders:
		wonder.displayInformation()

	print("\n" + "=" * 72)
	print("                         END OF TOUR")
	print("=" * 72)
	display_images(wonders)


if __name__ == "__main__":
	main()
