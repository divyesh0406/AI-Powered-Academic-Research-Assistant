from flask import Flask, render_template, request
import pandas as pd
# from M_summarizer import get_summary
from datetime import datetime
from webscrape import arxivscrape, downloadpdf #, preprocess
from M_pdfscrape import pdfscrape
from M_ImageCapScrape import extract_images_and_captions
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'OnlyPDFs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
titles = []

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/summary", methods=['GET', 'POST'])
def summary():
    global titles
    if request.method == "POST":
        topic = request.form["input"]
        arxivscrape.scrape(topic)
        df = pd.read_csv("Scrape.csv")
        titles = []
        for i in range(3):
            titles.append(df.iloc[i,0])
        csv_file = "OnlyURL.csv"
        base_filename = "NewPdf"
        target_folder = "OnlyPDFs"
        downloadpdf.download_all_pdfs(csv_file, base_filename, target_folder)

        for i in range(3):
            pdfscrape(f'{base_filename}{i}')

        textFile = 'text/' + base_filename + '.txt'
        cleanText = base_filename + '_cleaned' + '.txt'
        # preprocess.clean_data(textFile, cleanText)

        current_dateTime = datetime.now()
        inputs = []
        for i in range(3):
            print(current_dateTime)
            # newInput = get_summary(f'text/{base_filename}{i}.txt')
            # inputs.append(newInput)
            current_dateTime = datetime.now()
            print(current_dateTime)
    inputs = None
    if not inputs:
        # titles = ["Paper 1", "Paper 2", "Paper 3"]
        # inputs = ["ABDC content", "ABD content", "Ag content"]
        inputs = ['''attention alignment flexible positional embeddings improve transformer length extrapolation tachung chi carnegie mellon university tachungcandrew.cmu.edu tinghan fan independent researcher tinghanfalumni.princeton.edu alexander rudnicky carnegie mellon university aircs.cmu.edu abstract ideal lengthextrapolatable transformer lan guage model handle sequences longer training length long sequence finetuning. longcontext utilization pability highly relies flexible positional embedding design. investigating flex ibility existing large pretrained transformer language models, find family deserves closer look, positional embed dings capture rich flexible attention pat terns. however, suffers dispersed attention issue longer input sequence, flatter attention distribution. alleviate issue, propose attention alignment strategies temperature scaling. findings improve longcontext utilization capabil ity language modeling, retrieval, multidocument question answering finetuning, suggesting flexible sitional embedding design attention align ment long way transformer length extrapolation.1 introduction pretraining large transformer language models long sequences inherently expensive selfattentions quadratic complexity w.r.t sequence length vaswani al., 2017. help memoryefficient attention rabe staats, 2021 dao al., 2022, maximum supported input length current opensource pre trained transformer language models capped 4,096 tokens touvron al., 2023, limiting efficacy handling longcontext tasks. notable research topic aiming lift input length restriction length extrapo lation press al., 2022. ideally, length extrapolatable transformer language model trained short sequences perform equally 1httpsgithub.comchijames retrieval''', '''al., 2023. circumvent recency bias, sift positional embeddings existing opensource large pretrained transformer language models table find flexible design, fam ily raffel al., 2020 comes attention. visualized figure flexibility t5s posi tional embeddings allows encourage recency bias head discourage head. however, free lunch suffers dispersed attention issue shown ble nutshell, attention distributions long input sequences tend flatter short input sequences. remedy, propose finetuningfree attention alignment strategies softmax temperature scaling yao al., 2021 su, 2021 mitigate dispersed attention sue maximum probability pmax entropy alignment. attentionalignmenttransformerlengthextrapolation validate effectiveness alignment models 2020 opt 2022 chatglm 2022 llama 2023 falcon 2023 pythia 2023 xgen 2023 bloom 2022 mpt 2023 pe. learned learned relative absolute rotary relative rotary relative rotary relative rotary relative rotary relative alibi relative alibi relative table opensource transformer language models positional embeddings. model equipped learnable relative positional embeddings, enable longcontext utilization capability. strategies tasks including language model ing, retrieval, multidocument question answer ing. provide theoretical analysis alignment strategies work hood investigating relation softmax tem perature data distribution. related work transformer embeddings positional transformerbased models rely positional embeddings encode positional information. summarize opensource large pretrained transformer language models positional embeddings table relative variants widely adopted better empirical performance al., 2021 possible lengthextrapolatable capability press al., 2022. work, special focus positional embeddings flexibility shown figure transformer length extrapolation existing research transformer length extrapolation task natural language mod eling press al., 2022 chi al., 2022, 2023. unfortunately, reported positive results carry task longcontext retrieval htashami jaggi, 2023 al., 2023. contrastive observation explained mod els short empirical receptive field chi al., 2023. short, strong decaying prior positional beddings prevents models accessing faraway tokens necessary retrieval tasks. work, improve flexible positional embed dings limitation. transformer position interpolation instead performing direct length extrapolation, line research conducts model finetuning long input sequences chen al., 2023, main focus identify efficient fine tuning scheme improves longcontext utiliza tion. positive results reported retrieval tasks al., 2023. however, argue finetuning incurs additional costs needs gpu resources perform long sequence fine tuning large models predefined target sequence length, imposes sequence length upper limit. proposed methods cir cumvent limitations. tasks retrieval transformers transformerbased approaches consist retriever reader overcome context length restriction guu al., 2020 lewis al., 2020 izacard grave, 2021 borgeaud al., 2022. retriever retrieves relevant text snippets huge database reader digests retrieved information generate correct output. proposed attention alignment strategy significantly increase input sequence length reader, allowing retrieved information participate decision process. smallscale retrieval problems, methods obviates need context segmentation external keyvalue store prior work mohtashami jaggi, 2023, serving elegant approach. softmax temperature scaling increase length extrapolation capability transformers, previous work yao al., 2021 su, 2021 scales temperature softmax logarithmically w.r.t sequence length ensure invariant entropy. entropy alignment strategy inspired line research adopt differ ent procedure outlined later algorithm inter estingly, experiment results 5.2 aligning entropy performs worse proposed maximum probability alignment strategy. longcontext retrieval tasks 3.1 retrieval suggested recent work mohtashami jaggi, 2023 al., 2023, task long context retrieval serves controllable bench mark measure transformer language model utilizes longcontext inputs. prominent characteristic retrieval tasks subset input interest, requiring model accu 1st attention head 27nd attention head figure visualization positional embeddings. plot figures bm,n, set 7500 vary value 15k. attention head flant5xl encoder learns set positional embeddings capture different attention bias. example, positional embeddings left figure encourage model focus nearby tokens. contrast, ones right figure let model focus remote tokens. rately pick necessary information. characteristic key information sit input, requiring model attend flexibly. finally, controllable aspect allows gradually increase input sequence length test models length extrapolation capability. 3.2 solve retrieval tasks transformer language models, necessary choose positional bedding design permits accurate flexible lengthextrapolatable attention. checking existing positional embeddings ble find family raffel al., 2020 fits needs. candidates, learnable abso lute positional embeddings vaswani al., 2017 zhang al., 2022 evaluated training length. alibi press al., 2022 tary al., 2021 recency bias, extrapolate easily finetuning. attention head, encoder maintains bucket learnable parameters assigns relative ''', '''2httpsgithub.comhuggingfacetransformers blobv4.33.2srctransformersmodelst5 modelingt5.pyl390 entry selfattention matrix. summation input temperature scaled softmax. plot learned rpe bias encoder figure tell attention heads encode rich attention patterns. example, head learns focus nearby tokens head learns ignore nearby tokens allow access faraway tokens. 3.3 dispersed attention issue encoder unfortunately, directly applying models trieval tasks yield perfect results. inspecting intermediate model states, find longer input sequence consists kens competing i.e., softmax sums attention, resulting dispersed tention issue. table longer input sequence, flatter selfattention distri bution. situation hopeless desired information attains higher attention weight remaining tokens. proposed solution let key information stand out. proposed methods natural solution dispersed attention issue described sharpen selfattention dis tribution, achieved reducing temperature extrapolation. set trapolation temperature ex sharpness training tr extrap olation ex roughly same. measurement sharpness, explore maxi algorithm attention alignment strategies require short sequence length ltr long sequence length lex. encoder align ment mode ensure softmax temperature function finds 0.5. outline procedure alignment strategies algorithm note proposed methods require model finetuning gradient updates. model family pretrained sequences length 512, set ltr 512 experiments paper. set temperature softmax operation perform operation operation softmax maximum probability append maxsoftmax entropy append hsoftmax end end end return avgs end function str1 finds1.0, ex 1.0, 0.95, 0.9, 0.5 sexex findsex, end return ex s.t. sexex str1 mum probability entropy distribution. words, proposed solution align maximum probability entropy training extrapolation distributions adjusting ex. concretely, let ith presoftmax logit vector encoder, ltr, lex sequence length. postsoftmax distri bution pi softmax li. maximum probability entropy pi max hi respectively. let maximum probability alignment strategy example. run ward pass compute averaged maximum probability temperature logit vec tors pmax cid80 max number logit vectors encoder layers, heads, length sequences. temperature training ex extrapolation, denote averaged maximum probability train ing ptr max1 extrapolation pex maxex. finally, align maximum probabil ity, adjust ex pex max1. practice, grid search ex 1.0 maxex ptr experiments 5.1 language modeling following previous work transformer length extrapolation, perform intrinsic evaluation language modeling press al., 2022 chi al., 2022, 2023. ideally, proposed methods alleviate perplexity explosion problem hap pens extrapolation. ble alignment strategies dramatically prove lower perplexity. want empha size perplexity primary focus attempt surpass previous work metric lower perplexity accu rately reflect longcontext utilization capability transformers practical tasks al., 2023. models sequence length 1024 2048 4096 8192 15000 52.7 56.0 50.0 63.4 44.3 43.8 t5largelm 35.9 40.1 pmax 34.7 45.5 45.2 45.5 40.2 43.9 45.6 54.6 t5xllm 28.3 pmax 30.2 36.0 31.6 41.7 30.4 36.8 38.4 53.3 t5xxllm 109 pmax 32.2 29.7 29.5 36.6 26.8 28.1 34.2 37.8 table language modeling performance. numbers perplexity. lower better. use adapted models experiment.3 5.2 longcontext retrieval inspired recently proposed retrieval tasks, evaluate proposed alignment strategies retrieval tasks. topic retrieval requires model retrieve topic long multitopic con versation al., 2023. line retrieval long series keyvalue pairs, model needs trieve value corresponding given key al., 2023. passkey retrieval hides passkey 3httpsgithub.comgoogleresearch texttotexttransfertransformerblobmain releasedcheckpoints.mdlmadaptedt511lm100k retrieval tasks models line, lines topic, topics 100 flant5large 100 pmax 100 100 100 100 100 flant5xl pmax 100 100 100 100 100 100 100 flant5xxl 100 100 100 pmax 100 100 100 100 100 100 100 100 100 longchat passkey, sentences 200 300 400 500 600 680 20k 30k 40k 50k 55k 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 avg. table performance retrieval tasks. numbers accuracy. score 100. longchat model corresponds longchat13b16k model al., 2023. llama13b touvron al., 2023 model finetuned sequences length 16k positional interpolation technique chen al., 2023. flant5xxl 11b parameters. maximum lengths tasks 14.5k 15k tokens. topic, topics flant5xl pmax 200 300 400 500 600 680 20k 30k 40k 50k 55k 0.8 0.75 0.7 0.65 0.65 0.8 0.75 0.75 0.7 0.70 0.7 0.85 0.8 0.75 0.75 0.75 0.7 0.55 0.55 0.5 0.5 0.6 0.55 0.55 0.5 0.5 0.5 0.7 0.65 0.6 0.6 0.6 retrieval tasks line, lines passkey, sentences table temperatures retrieval tasks. search optimal temperature 1.0, 0.95, 0.9, 0.5. long junk text snippet, model needs return passkey mohtashami jaggi, 2023. tasks formulated question swering format, use flant5 models leverage instructionfollowing capability. table retrieval perfor mance greatly boosted flant5 models equipped proposed attention alignment strategies. particular, maximum probability alignment strategy gives better results board. note longchat al., 2023, best baseline, finetuned llama tou vron al., 2023 long sequences length 16k proposed methods need fine tuning. baselines mpt team, 2023 chatglm2 al., 2022 perform worse longchat. refer al. 2023 details. present optimal temperature given algorithm table see, temperature decreases input quence length increases. temperatures model sizes highly similar ones presented table find table appendix conduct temperature analysis later 6. 5.3 multidocument question answering choose multidocument question answer ing task downstream task liu al., 2023. model input consists questions multiple documents extracted naturalques tions kwiatkowski al., 2019 documents golden doc contains ground truth answer. table model equipped proposed maximum probability alignment strategy, consistently outperforms original model model sizes number input documents. apart better task performance, lieve attention dispersed attention issue dis cussed help demystify lostinthe middle phenomenon liu al., 2023 task transformer models tend perform worse ground truth sits near middle input context. let recall relative positional embed ding head learned figure ground truth answer sits middle, long models flant5large pmax improvement flant5xl pmax improvement flant5xxl pmax improvement docs avg. 52.4 53.1 0.7 52.1 59.4 61.1 1.7 60.5 63.6 63.7 0.1 63.6 33.9 35.9 36.5 39.5 docs, golden doc different positions multidocument question answering docs avg. 43.3 44.2 0.9 43.2 51.2 53.6 2.4 52.4 56.9 57.7 0.8 57.1 37.9 42.0 34.0 33.9 52.6 37.0 35.8 36.4 44.5 50.8 0.9 1.5 3.0 2.4 2.0 1.9 1.8 34.2 33.3 33.5 41.1 47.6 54.8 46.4 39.9 44.6 58.4 60.9 55.7 49.1 44.9 49.1 2.5 4.5 6.0 5.0 4.6 2.7 0.9 42.9 51.3 40.3 52.4 53.1 61.2 47.5 58.9 59.1 60.4 53.5 50.2 2.1 1.5 3.4 2.9 2.7 2.4 0.4 55.7 51.9 61.0 35.2 40.0 46.0 42.1 48.1 51.0 32.2 41.7 46.3 43.5 49.1 52.5 42.0 48.9 51.3 50.7 50.3 53.4 50.8 avg. 38.7 40.0 1.3 36.7 46.5 50.3 3.8 44.9 52.4 54.0 1.6 53.4 table performance multidocument qa. numbers accuracy. score 100. improvement row represents absolute accuracy improvement flant5 model equipped proposed maximum probability alignment strategy. performance breakdown, refer table appendix contexts sides competing atten tion weight. hypothesis holds true, expect performance boost prominent cases answer sits near middle. reveal performance breakdown number input documents 30. provement row, cases achieve greater improvement. strategies perfect formance drops ground truth answer position 29. believe han dled case pretty recency bias learned attention heads, additional temperature scaling sharpens distribution aggressively. acknowledge tradeoff 8. 5.4 overall observation maximum probability alignment strategy reliable bestperforming method tasks settings, echoing discussion 3.1 data, subset input useful. maximum probability alignment strat egy captures characteristic naturally, outperforming entropy alignment strategy cares holistic distribution. theoretical analysis shed light underlying mechanisms alignment strategies, establish connection softmax temperature data distribution empirically verified assump tions. focus 0th layer closest input embeddings average logit vectors attention heads. note crude approximation algorithm analysis purposes transformer language model typically encompasses multiple layers, algorithm maximum probabil ity entropy individual logit vectors opposed averaged one. compute averaged logit vector, start input sequence length trans model attention heads specifically, encoder context, generate presoftmax logit vectors, length here, number layers focus 0th layer. logit vectors indi vidually sorted, subsequently calculate average sorted logit vectors, resulting averaged logit vector length assumption length averaged logit vector normally distributed, i.e., entry 2. assess averaged logit entries fol low gaussian distribution, employ plots, illustrated figure plot wilk gnanadesikan, 1968 graphical technique comparing probability distributions plot ting quantiles other. point corresponds quantile second dis tribution ycoordinate plotted quantile distribution xcoordinate. short sequences 512 long sequences 15k figure plots flant5xl. experiment short long sequences. red reference line yx. retrieval tasks line topic passkey 512 8.61 15k 8.80 512 8.71 15k 8.97 512 8.75 15k 8.85 ''']
    return render_template("summary.html", titles=titles, inputs=inputs)

@app.route("/images")
def images():
    global titles
    base_filename = "NewPdf"
    target_folder = "OnlyPDFs/"
    pdf_location = target_folder + base_filename
    
    images_caption = []
    if len(titles) == 1:
        images_caption.append(extract_images_and_captions(f'{target_folder + titles[0]}.pdf'))
    else:
        for i in range(len(titles)):
            images_caption.append(extract_images_and_captions(f'{pdf_location}{i}.pdf'))
            # images_caption[i] = extract_images_and_captions(f'{pdf_location}{i}.pdf')
            # for i in range(0,len(images_caption)):
            #     for k, v in images_caption[i].items():
            #         print(k)

    return render_template("images.html", images_caption = images_caption, data_length = len(images_caption), titles= titles)

    # counter = 7
    # return render_template("images.html", counter=counter+1)

@app.route("/upload", methods=("GET","POST"))
def upload():
    if request.method == "POST":
        pdf = request.files.get("pdf")
        base_filename = pdf.filename[:-4]
        pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
        pdfscrape(base_filename)

        textFile = 'text/' + base_filename + '.txt'
        cleanText = base_filename + '_cleaned' + '.txt'
        # preprocess.clean_data(textFile, cleanText)

        current_dateTime = datetime.now()

        print(current_dateTime)
        # inp = get_summary(textFile)
        titles.clear()
        titles.append(base_filename)
        inp = "ABCD"
        inputs = []
        inputs.append(inp)
        current_dateTime = datetime.now()

        print(current_dateTime)

    return render_template("summary.html", titles=titles, inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)
