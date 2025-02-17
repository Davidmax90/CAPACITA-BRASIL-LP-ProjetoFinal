def jogo_da_forca(palavra_secreta):
    """Lógica principal do jogo da forca."""
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6 
    
    
    while tentativas > 0:
        print("\nPalavra:", " ".join(letra if letra in letras_certas else "_" for letra in palavra_secreta))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")
        
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("❌ Entrada inválida! Digite apenas uma letra.")
            continue

        if tentativa in letras_certas or tentativa in letras_erradas:
            print("❌ Você já tentou essa letra. Escolha outra.")
            continue

        if tentativa in palavra_secreta:
            letras_certas.add(tentativa)
            print("✅ Boa! A letra está na palavra.")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print("❌ Errou! Essa letra não está na palavra.")

        if set(palavra_secreta) == letras_certas:
            print(f"\n🏆 Parabéns! Você acertou a palavra: {palavra_secreta.upper()} 🏆")
            break
    else:
        print(f"\n💀 Você perdeu! A palavra era: {palavra_secreta.upper()}")