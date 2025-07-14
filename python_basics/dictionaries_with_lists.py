speakers = {
    "Rohan Johnson": ["Python Best Practices", "Machine Learning Intro"],
    "Bob Smith": ["Cybersecurity Fundamentals", "Blockchain 101"],
    "Rajan Lee": ["Data Visualization Techniques", "Advanced SQL Queries"],
}
for speaker, topics in speakers.items():
    print(f"{speaker} will talk:")
    for topic in topics:
        print(f"-{topic}")
