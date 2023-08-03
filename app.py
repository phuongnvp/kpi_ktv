import streamlit as st

def calculate_points(box1_value, box2_value, box3_value, box4_value, box5_value, box6_value, box7_value, box8_option, box9_option, box10_value, box11_value, box12_value, box13_option, box14_value, box15_option, box16_value, box17_value, box18_value, box19_value):
    plus1 = 0
    plus2 = 0
    # Calculate points for Box 1 based on ranges
    if box1_value >= 330:
        box1_points = 35
        plus1 = 5
    elif 302 <= box1_value <= 329:
        box1_points = 35
        plus1 = 3
    elif 288 < box1_value <= 301:
        box1_points = 35
        plus1 = 2
    elif 274 <= box1_value <= 287:
        box1_points = 35
        plus1 = 0
    elif 247 <= box1_value <= 273:
        box1_points = 33
        plus1 = 0
    elif 219 <= box1_value <= 246:
        box1_points = 30
        plus1 = 0
    elif 192 <= box1_value <= 218:
        box1_points = 26
        plus1 = 0
    elif 165 <= box1_value <= 191:
        box1_points = 23
        plus1 = 0
    elif 137 <= box1_value <= 164:
        box1_points = 19
        plus1 = 0
    elif 110 <= box1_value <= 137:
        box1_points = 16
        plus1 = 0
    else:
        box1_points = 0
        plus1 = 0

    # Calculate points for Box 2 to Box 7
    box2_points = box2_value
    box3_points = box3_value
    box4_points = box4_value
    box5_points = box5_value
    box6_points = box6_value
    box7_points = box7_value

    # Assign points based on the selected option for Box 8
    if box8_option == 'Đảm bảo đầy đủ các đợt thực tập':
        box8_points = 3
    else:
        box8_points = 0

    # Assign points based on the selected option for Box 9
    if box9_option == 'Đảm bảo chất lượng tất cả các đợt thực tập':
        box9_points = 5
    else:
        box9_points = 0

    # Calculate points for Box 10 based on ranges
    if box10_value >= 491:
        box10_points = 31
        plus2 = 5
    elif 446 <= box10_value <= 490:
        box10_points = 31
        plus2 = 3
    elif 409 <= box10_value <= 445:
        box10_points = 31
        plus2 = 1
    elif box10_value == 408:
        box10_points = 31
        plus2 = 0
    elif 367 <= box10_value <= 407:
        box10_points = 29
    elif 326 <= box10_value <= 366:
        box10_points = 26
    elif 285 <= box10_value <= 325:
        box10_points = 23
    elif 245 <= box10_value <= 284:
        box10_points = 20
    elif 204 <= box10_value <= 244:
        box10_points = 17
    elif 163 <= box10_value <= 203:
        box10_points = 14
    else:
        box10_points = 0

    box11_points = 2*box11_value
    box12_points = box12_value

    # Assign points based on the selected option for Box 13
    if box13_option == 'Tích cực đóng góp ý kiến, góp ý văn bản':
        box13_points = 6
    else:
        box13_points = 4

    box14_points = box14_value

    if box15_option == 'Thực hiện đầy đủ':
        box15_points = 2
    elif box15_option == 'Có 01 lần để xảy ra lỗi đến mức bị ghi thành Biên bản':
        box15_points = 1
    else:
        box15_points = 0
    
    box16_points = box16_value
    box17_points = box17_value
    box18_points = box18_value
    box19_points = box19_value
    
    return box1_points + box2_points + box3_points + box4_points + box5_points + box6_points + box7_points + box8_points + box9_points + box10_points + max(6-box11_points-box12_points, 0) + max(box13_points - box14_points,0) + box15_points + plus1 + plus2 + box16_points + box17_points + box18_points + box19_points

def main():
    st.title('Kết quả tự đánh giá KPI Kỹ thuật viên')

    # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>1. Công tác chuẩn bị và phục vụ thực tập</h1>", unsafe_allow_html=True)

    # Second-level header
    st.markdown("<h2 style='font-size: 20px;'>1.1. Hoàn thành định mức giờ phục vụ thực tập</h2>", unsafe_allow_html=True)

    box1_value = st.text_input('Số buổi phục vụ thực tập (Định mức 274 buổi):')
    
    # Second-level header
    st.markdown("<h2 style='font-size: 20px;'>1.2. Chất lượng hoạt động phục vụ thực tập</h2>", unsafe_allow_html=True)
    st.write('_Vui lòng nhập số điểm tự đánh giá tương ứng!_')
    box2_value = st.text_input('Có mặt đúng giờ và thường xuyên trong quá trình thực tập (Tối đa 2 điểm):')
    box3_value = st.text_input('Hỗ trợ hướng dẫn sinh viên, học viên kịp thời và đầy đủ trong quá trình thực tập về các thao tác thí nghiệm (Tối đa 5 điểm):')
    box4_value = st.text_input('Đảm bảo vệ sinh dụng cụ, thiết bị, phòng thực tập sạch sẽ, đạt tiêu chuẩn (Tối đa 2 điểm):')
    box5_value = st.text_input('Đảm bảo nhãn các chai lọ đựng dung dịch đúng quy định, đầy đủ thông tin (Tối đa 1 điểm):')
    box6_value = st.text_input('Bổ sung dụng cụ, hóa chất kịp thời trong quá trình thực tập (Tối đa 1 điểm):')
    box7_value = st.text_input('Đảm bảo về an toàn lao động trong quá trình thực tập: không xảy ra cháy nổ trong thực tập; xử lý đúng, kịp thời khi xảy ra cháy nổ trong thực tập, đảm bảo dụng cụ y tế, cấp cứu đầy đủ (Tối đa 1 điểm):')

    # Second-level header
    st.markdown("<h2 style='font-size: 20px;'>1.3. Công tác chuẩn bị cho thực tập</h2>", unsafe_allow_html=True)

    # Option for Box 8
    box8_option = st.selectbox('Đảm bảo đầy đủ, kịp thời dung dịch chuẩn, thuốc thử, động vật thực nghiệm trước mỗi đợt thực tập', ['Đảm bảo đầy đủ các đợt thực tập', 'Chuẩn bị thiếu theo phân công cho một đợt'])

    # Option for Box 9
    box9_option = st.selectbox('Đảm bảo dung dịch chuẩn, thuốc thử pha chế đạt tiêu chuẩn quy định; không làm ảnh hưởng đến kết quả thực tập của SV; Đảm bảo chăm sóc động vật thí nghiệm an toàn, khỏe mạnh', ['Đảm bảo chất lượng tất cả các đợt thực tập', 'Có 1 đợt thực tập có hóa chất, thuốc thử, động vật thí nghiệm không đạt tiêu chuẩn, làm ảnh hưởng đến kết quả thực tập của sinh viên'])

    
    # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>2. Thực hiện công việc hỗ trợ công tác giáo tài, giáo vụ, hành chính Khoa và thực hiện công việc phục vụ PTN cho NCKH</h1>", unsafe_allow_html=True)

    # Option for Box 10
    box10_value = st.text_input('Số giờ thực hiện (Định mức 408 giờ):')
    
    # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>3. Công tác coi thi</h1>", unsafe_allow_html=True)

    box11_value = st.text_input('Số lần vi phạm nghiệp vụ coi thi:')

    box12_value = st.text_input('Số lần quên coi thi bị ghi nhận trong thông báo kết quả thanh tra thi của Phòng ĐBCL và Khảo thí:')

   # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>4. Thực hiện công việc chung (họp, tập huấn...)</h1>", unsafe_allow_html=True)

    # Option for Box 13
    box13_option = st.selectbox('Tham gia công việc chung', ['Tích cực đóng góp ý kiến, góp ý văn bản', 'Chưa tích cực đóng góp ý kiến, góp ý văn bản'])

    box14_value = st.text_input('Số lần vắng mặt không được sự đồng ý của Trưởng/Phụ trách Khoa:')

    # First-level header
    st.markdown("<h1 style='color: yellow; font-size: 24px;'>5. Thực hiện công việc khác Trường giao</h1>", unsafe_allow_html=True)

    box15_option = st.selectbox('Thực hiện công việc khác Trường giao', ['Thực hiện đầy đủ', 'Có 01 lần để xảy ra lỗi đến mức bị ghi thành Biên bản', 'Có 02 lần trở lên để xảy ra lỗi đến mức bị ghi thành Biên bản'])

    # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>6. Điểm thưởng</h1>", unsafe_allow_html=True)
    st.write('_Vui lòng nhập số điểm tự đánh giá tương ứng!_')
    box16_value = st.text_input('Tham gia công tác quảng bá tuyển sinh, hội chợ tuyển sinh của Trường ĐH Dược Hà Nội (Tối đa 1 điểm):')
    box17_value = st.text_input('Có sáng kiến trong công việc đem lại hiệu quả được công nhận (Tối đa 5 điểm):')
    box18_value = st.text_input('Tham gia công tác tình nguyện, trừ hoạt động hiến máu nhân đạo (Tối đa 2 điểm):')
    box19_value = st.text_input('Tham gia công tác hiến máu nhân đạo ít nhất 1 lần/năm (Tối đa 2 điểm):')
    
    if st.button('Calculate'):
        try:
            box1_value = int(box1_value)
            box2_value = int(box2_value)
            box3_value = int(box3_value)
            box4_value = int(box4_value)
            box5_value = int(box5_value)
            box6_value = int(box6_value)
            box7_value = int(box7_value)
            box10_value = int(box10_value)
            box11_value = int(box11_value)
            box12_value = int(box12_value)
            box14_value = int(box14_value)
            box16_value = int(box16_value)
            box17_value = int(box17_value)
            box18_value = int(box18_value)
            box19_value = int(box19_value)
            
            total_points = calculate_points(box1_value, box2_value, box3_value, box4_value, box5_value, box6_value, box7_value, box8_option, box9_option, box10_value, box11_value, box12_value, box13_option, box14_value, box15_option, box16_value, box17_value, box18_value, box19_value)
            st.write(f'Tổng điểm KPI: {total_points}')
            if total_points >= 105:
                st.write('Hoàn thành xuất sắc nhiệm vụ')
            elif 85 <= total_points < 105:
                st.write('Hoàn thành tốt nhiệm vụ')
            elif 70 <= total_points < 85:
                st.write('Hoàn thành nhiệm vụ')
            else:
                st.write('Không hoàn thành nhiệm vụ')
        except ValueError:
            st.error('Vui lòng kiểm tra và nhập lại thông tin.')

if __name__ == '__main__':
    main()
