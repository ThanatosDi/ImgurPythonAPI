# ImgurPythonAPI

## 安裝
   * 安裝套件  
    `python -m pip install -r requirements.txt`  
    
   * 匯入API  
    `from ImgurPythonAPI.Imgur import Imgur`
## 使用
當操作不需要認證時 refresh_token 可以保持為空，但需要認證的操作就需要 refresh_token  
* 不需認證
```python
client_id = '123456789'
client_secret = '123456789asdzxcqwe123456'
Client = Imgur(client_id, client_secret)
Data = Client.Album('EPGUzgm')
print(Data)
```
* 需要認證
```python
client_id = '123456789'
client_secret = '123456789asdzxcqwe123456'
refresh_token = '5648444sd8g4sd8g445asf88awf44'
Client = Imgur(client_id, client_secret, refresh_token)
Data = Client.Account('username')
print(Data)
```
## Functions
目前還尚未完成，現階段只完成部分功能，一般回傳格式為 dict

  *  ### 帳號 Account
     *  #### Get_token()
          不需驗證  
          取得 refresh_token，回傳網址請在瀏覽器開啟
     *  #### Refresh_token()
          需驗證  
          重新取得 access_token(一個月後過期) 及 refresh_token(據說不會過期)
     *  #### Account('username')
          不需驗證  
          取得 username 帳號資料
     *  #### Account_Block_Status('username')
          不需驗證  
          取得 username 帳號封鎖狀態
     *  #### Account_Blocks('username')
          需驗證  
          取得 username 封鎖列表
     *  #### Account_Images()
          需驗證  
          取得帳號的圖片
  *  ### 評論 Comment
  *  ### 相片簿(專輯) Album
     *  #### Album('album_id')
          不需驗證  
          取得相片簿(專輯)的資料
     *  #### Album_Images('album_id')
          不需驗證  
          取得相片簿(專輯)的圖片
     *  #### Album_Images_Detail('album_id', 'image_id')
          不需驗證  
          取得相片簿(專輯)中的某圖片詳細資料
  *  ### 畫廊 Gallery
  *  ### 圖片 Image
       *  #### Image_Upload(image, auth=False, Optional)
          不需驗證 auth=False、需驗證 auth=True  
          上傳圖片  
          (Optional)  
             * album  
                The id of the album you want to add the image to.
             * type  
                file, base64 or URL.
             * name  
                The name of the file.
             * title  
                The title of the image.
             * description  
                The description of the image.
       *  #### Image_Delete('image_id')
          需驗證  
          刪除指定圖片
       *  #### Image_Delete_AM('image_deletehash')
          不需驗證，但需要 deletehash 上傳圖片時會取得  
          刪除指定圖片
