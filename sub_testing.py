import ID_finder as id
import Sub_downloader as sd


sd.yt_search("1OnBVqeW5JA", "how many people", True)

keepGoing=True
while keepGoing:

	for each in id.JRE_ids[65:90]:
		print(each)
		sd.yt_search(each, "mental diet", True)
		keepGoing=False

print(id.JRE_ids.index("1OnBVqeW5JA"))