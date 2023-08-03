import streamlit as st
import pdfkit
import os

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
    
    st.markdown("<h1 style='color: violet; font-size: 28px;'>Phần 1. Quy đổi giờ các hình thức hoạt động</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: red; font-size: 24px;'>1. Quy đổi giờ phục vụ thực tập</h1>", unsafe_allow_html=True)    
    box20_value = st.text_input('Số tổ thực tập:')
    box21_value = st.text_input('Số bài thực tập')
    box22_value = st.text_input('Số ngày chuẩn bị thực tập')
    box23_value = st.text_input('Số ngày điều động hỗ trợ các phòng chức năng')
    if st.button('Tính giờ phục vụ thực tập'):
        try:
            box20_value = float(box20_value)
            box21_value = float(box21_value)
            box22_value = float(box22_value)
            box23_value = float(box23_value)
            
            TT_point = (box20_value + 3 * box23_value) * box21_value + 8 * box22_value
            st.session_state.box1_value = TT_point
            st.write(f'Tổng giờ phục vụ thực tập: {TT_point}')
        except ValueError:
            st.error('Vui lòng kiểm tra và nhập lại thông tin.')

    st.markdown("<h1 style='color: red; font-size: 24px;'>2. Quy đổi giờ đối với các hình thức hoạt động khác</h1>", unsafe_allow_html=True)    
   
    st.markdown("<h2 style='font-size: 20px;'>2.1. Công tác hành chính</h2>", unsafe_allow_html=True)
    box33_value = st.text_input('Thư ký các buổi họp giao ban khoa (số buổi)')
    box34_value = st.text_input('Tập hợp thông tin và soạn thảo văn bản để báo cáo, trả lời công văn Nhà trường (số trang)')
    box35_value = st.text_input('Tiếp nhận và bàn giao công văn trong Trường (số công văn)')
    box36_value = st.text_input('Tiếp nhận và bàn giao công văn ngoài Trường (số công văn)')
    box37_value = st.text_input('Quản lý văn phòng phẩm (số tháng)')
    box38_value = st.text_input('Phục vụ hậu cần Khoa (số tháng)')
    box39_value = st.text_input('Hỗ trợ nhập điểm thành phần với lớp 60 sinh viên (số đầu điểm)')
    box40_value = st.text_input('Hỗ trợ nhập điểm thành phần với lớp 170-200 sinh viên (số đầu điểm)')
    box41_value = st.text_input('Hỗ trợ nhập thời khóa biểu trên phần mềm, phân công lịch thực tập cho KTV (số lớp)')
    box42_value = st.text_input('Hỗ trợ nhập thông tin và kiểm tra thông tin trên phần mềm đánh giá năng lực giảng viên, KTV (số buổi). Tối đa 2 buổi/kỳ x 2 kỳ/năm')
    box43_value = st.text_input('Hỗ trợ quản lý công văn giấy tờ Bộ môn (số tháng)')
    box44_value = st.text_input('Hỗ trợ quản lý công văn của Khoa (số tháng)')
    box45_value = st.text_input('Hỗ trợ Khoa trong công tác tài chính (số tháng)')
    box46_value = st.text_input('Hỗ trợ Khoa chấm công (số tháng)')
    box47_value = st.text_input('Hỗ trợ theo dõi, gửi, thông báo các văn bản, tin tức liên quan trong nội bộ Khoa (số tuần)')

    st.markdown("<h2 style='font-size: 20px;'>2.1. Công tác giáo tài</h2>", unsafe_allow_html=True)
    box28_value = st.text_input('Phối hợp Giáo tài hoàn thành Dự trù TTB, hóa chất phục vụ cho bài thực tập. Số giờ dự trù hóa chất, dụng cụ phục vụ cho 1 bài thực tập (số bài thực tập)')
    box29_option = st.selectbox('Tiếp nhận hóa chất, dụng cụ cho bài thực tập cùng giáo tài', ['Có', 'Không'])
    box30_option = st.selectbox('Hỗ trợ giáo tài lưu trữ, kiểm kê, định kỳ bảo quản hóa chất, dụng cụ, vật tư tiêu hao phục vụ thực tập và nghiên cứu', ['Có', 'Không'])
    box31_value = st.text_input('Kiểm tra nhật ký sử dụng thiết bị (số thiết bị/năm)')
    box32_value = st.text_input('Chuẩn bị dụng cụ hóa chất để giảng viên phụ trách thiết bị vận hành kiểm tra định kỳ (số học kỳ)')

    st.markdown("<h2 style='font-size: 20px;'>2.1. Công tác NCKH</h2>", unsafe_allow_html=True)
    box24_value = st.text_input('Thực hiện các hoạt động thực nghiệm phục vụ các đề tài NCKH tùy theo thỏa thuận với chủ trì đề tài (số buổi):')
    box25_value = st.text_input('Theo dõi việc sử dụng và ghi nhật ký sử dụng thiết bị, nhật ký PTN (số buổi):')
    box26_value = st.text_input('Giám sát học viên, NCV của đơn vị khác (số buổi):')
    box27_value = st.text_input('Kiểm tra tình trạng PTN sau khi nhóm nghiên cứu hoàn thành công việc trong ngày (số buổi):')
    
    if st.button('Tính giờ hỗ trợ hoạt động khác'):
        try:
            box24_value = float(box24_value)
            box25_value = float(box25_value)
            box26_value = float(box26_value)
            box27_value = float(box27_value)
            box28_value = float(box28_value)
            box31_value = float(box31_value)
            box32_value = float(box32_value)
            box33_value = float(box33_value)
            box34_value = float(box34_value)
            box35_value = float(box35_value)
            box36_value = float(box36_value)
            box37_value = float(box37_value)
            box38_value = float(box38_value)
            box39_value = float(box39_value)
            box40_value = float(box40_value)
            box41_value = float(box41_value)
            box42_value = float(box42_value)
            box43_value = float(box43_value)
            box44_value = float(box44_value)
            box45_value = float(box45_value)
            box46_value = float(box46_value)
            box47_value = float(box47_value)
            
            if box29_option == 'Có':
                box29_value = 4
            else:
                box29_value = 0

            if box30_option == 'Có':
                box30_value = 80
            else:
                box30_value = 0

            HC_point = 4 * (box24_value + box25_value + box26_value + box27_value) + box28_value + box29_value + box30_value + 6*box31_value + 4*box32_value + box33_value + 4*(box34_value+box37_value+box38_value+box42_value+box43_value+box44_value+box45_value+box46_value+box47_value) + 0.5*box35_value + 2*box36_value + box39_value + 3*box40_value + 2*box41_value
            st.session_state.box10_value = HC_point
            st.write(f'Tổng giờ hỗ trợ công tác giáo tài, giáo vụ, hành chính, NCKH: {HC_point}')
        except ValueError:
            st.error('Vui lòng kiểm tra và nhập lại thông tin.')


    st.markdown("<h1 style='color: violet; font-size: 28px;'>Phần 2. Tự đánh giá KPI</h1>", unsafe_allow_html=True)
    # First-level header
    st.markdown("<h1 style='color: red; font-size: 24px;'>1. Công tác chuẩn bị và phục vụ thực tập</h1>", unsafe_allow_html=True)

    # Second-level header
    st.markdown("<h2 style='font-size: 20px;'>1.1. Hoàn thành định mức giờ phục vụ thực tập</h2>", unsafe_allow_html=True)

    box1_value = st.text_input('Số buổi phục vụ thực tập (Định mức 274 buổi):', value=st.session_state.get('box1_value', ''))
    
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
    box10_value = st.text_input('Số giờ thực hiện (Định mức 408 giờ):', value=st.session_state.get('box10_value', ''))
    
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
    st.markdown("<h1 style='color: red; font-size: 24px;'>5. Thực hiện công việc khác Trường giao</h1>", unsafe_allow_html=True)

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
            box1_value = float(box1_value)
            box2_value = float(box2_value)
            box3_value = float(box3_value)
            box4_value = float(box4_value)
            box5_value = float(box5_value)
            box6_value = float(box6_value)
            box7_value = float(box7_value)
            box10_value = float(box10_value)
            box11_value = float(box11_value)
            box12_value = float(box12_value)
            box14_value = float(box14_value)
            box16_value = float(box16_value)
            box17_value = float(box17_value)
            box18_value = float(box18_value)
            box19_value = float(box19_value)
            
            total_point = calculate_points(box1_value, box2_value, box3_value, box4_value, box5_value, box6_value, box7_value, box8_option, box9_option, box10_value, box11_value, box12_value, box13_option, box14_value, box15_option, box16_value, box17_value, box18_value, box19_value)
            total_points = round(total_point, 2)
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

    
    # Add a button to generate the PDF
    if st.button("Generate PDF"):
        # Specify the file path to save the PDF
        pdfkit.from_url('https://kpi-ktv.streamlit.app/', 'KPI.pdf')
        st.success("PDF generated!")

    if os.path.exists('KPI.pdf'):
        with open('KPI.pdf', 'rb') as f:
            pdf_data = f.read()
        st.download_button("Download PDF", data=pdf_data, file_name='KPI.pdf', mime='application/pdf')

if __name__ == '__main__':
    main()