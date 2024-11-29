print("Pham Viet Quan mssv 235752021610022")
def find_longest_words(text):
    words = text.split()
    cleaned_words = [word.strip(".,!?;:()[]{}\"'") for word in words]
    max_length = max(len(word) for word in cleaned_words)
    longest_words = [word for word in cleaned_words if len(word) == max_length]
    return longest_words
text = """
Python là một ngôn ngữ lập trình tuyệt vời giúp giải quyết nhiều vấn đề phức tạp
với các giải pháp dễ dàng và hiệu quả. Nó được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học dữ liệu,
trí tuệ nhân tạo, học máy và phát triển web
"""
longest_words = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:", longest_words)
