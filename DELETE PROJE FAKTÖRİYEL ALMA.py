{
 "cells": [
  {
   "cell_type": "raw",
   "id": "bacab69c",
   "metadata": {},
   "source": [
    "Faktöriyel Alma\n",
    "\n",
    "Faktöriyel, 1'den başlayarak belirli bir sayma sayısına kadar olan sayıların çarpımıdır.\n",
    "Kullanıcı tarafından girilen değerin faktöriyelini alan programı yazınızı istiyorum. Programınız en az aşağıdaki gereksinimleri karşılasın;\n",
    "\n",
    "1) Faktoriyel işlemi için hazır matematik fonksiyonu kullanmayın. Döngü ile bu işlemi kendini kurgulayın.\n",
    "2) Hesaplama bittikten sonra sonuç ekrana basılsın, yeni hesaplama için kullanıcıdan tekrar değer istesin.\n",
    "3) Kullanıcı değer olarak \"q\" karkterini girerse program sonlansın.\n",
    "4) Kullanıcı giriş verilerinin doğrulaması olsun. 0-9 ve \"q\" harici veri girişlerininde \"hatalı giriş yaptınız\" uyarısı gelsin."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "46ee0356",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lütfen numerik bir değer giriniz: 5\n",
      "5 faktoriyeli: 120\n",
      "Lütfen numerik bir değer giriniz: d\n",
      "Hatalı giriş yaptınız.Lütfen numerik bir değer giriniz\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[1;32m----> 2\u001b[0m     deger \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mLütfen numerik bir değer giriniz: \u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m deger \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mq\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m      5\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDöngüden çıkıyorsunuz\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Local\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1202\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1200\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1201\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1202\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1203\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1204\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1205\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1206\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m   1207\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1245\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1242\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1243\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1244\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1245\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1246\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1247\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    deger = input(\"Lütfen numerik bir değer giriniz: \")\n",
    "\n",
    "    if deger == \"q\":\n",
    "        print(\"Döngüden çıkıyorsunuz\")\n",
    "        break\n",
    "\n",
    "    elif deger.isdigit():\n",
    "        \n",
    "        result = 1\n",
    "        for i in range(1,int(deger)+1):\n",
    "            result *= i\n",
    "        print(f\"{deger} faktoriyeli: {result}\")\n",
    "        \n",
    "    else:\n",
    "        print(\"Hatalı giriş yaptınız.Lütfen numerik bir değer giriniz\")\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51026575",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64b0ea81",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec0a2995",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
