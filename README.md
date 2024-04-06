<h1>GPT-2 TwitterBot</h1>

 ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo)

<h2>Description</h2>
My project facilitates the downloading of data from Twitter, enabling users to collect tweets from specific accounts. Subsequently, users can fine-tune a GPT-2 or other large language models using the collected data, allowing for personalized tweet generation. With my tool, users can effortlessly gather Twitter data, fine-tune models, and generate tweets tailored to their preferences.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>PyTorch</b>
- <b>HuggingFace<b/>

<h2>Environments Used </h2>

<h2>Program walk-through:</h2>

<p align="center">
1. Set your access api in auth_tw.py<br/>
 
 ![image](https://github.com/DataProfunda/GPT-2-TwitterBot/assets/69935274/bc42141c-bcf5-4a81-9486-f637c6d9a9fe)

<br />
<br />

<p align="center">
2. Add accounts that you want to base your generation on in get_user_tweets.py. <br/>

![image](https://github.com/DataProfunda/GPT-2-TwitterBot/assets/69935274/4da31bab-9047-42a7-bc99-b4e20c023602)
<br />
<br />
3. Fine-Tune LLM Model( by default GPT-2 ) <br/>

![image](https://github.com/DataProfunda/GPT-2-TwitterBot/assets/69935274/ef5d472f-93f4-4012-bdc5-f91fe2683f41)
<br />
<br />
4. Use fine-tuned model for tweets generation <br/>
Example of generated text
![image](https://github.com/DataProfunda/GPT-2-TwitterBot/assets/69935274/09c7bf74-3741-4bc7-8224-a6df520cae75)


<br />
<br />
5. Example tweet <br/>

![image](https://github.com/DataProfunda/GPT-2-TwitterBot/assets/69935274/1023c15b-ca53-45d7-9d9f-451d71d2ce4b)

</br>
</br>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
