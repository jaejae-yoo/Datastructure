subroutine median_filter(img, nf, h, w, blurImg)
integer, intent(in) :: h, w, nf
integer, intent(in) :: img(h,w,3)
integer, intent(out) :: blurImg(h-(nf-1), w-(nf-1),3)
integer temp(nf*nf)

nvoid = int(nf / 2)

do k = 1,3
    do i = nvoid+1, h-nvoid
        do j = nvoid+1, w-nvoid
            l = 1
            do ii = -nvoid, nvoid
                do jj = -nvoid, nvoid
                    temp(l) = img(i+ii, j+jj,k)
                    l =l+1
                end do
            end do
            call sort(temp, nf*nf, med)
            blurImg(i-nvoid, j-nvoid,k) =med
        end do
    end do
end do
return
end subroutine

subroutine gauss_filter(img, h, w, blurImg)
integer, intent(in) :: h, w
integer, intent(in) :: img(h,w,3)
integer, intent(out) :: blurImg(h-2,w-2,3)
integer :: gauss(9), summ
gauss(1)= 1
gauss(2)= 2
gauss(3)= 1
gauss(4)= 2
gauss(5)= 4
gauss(6)= 2
gauss(7)= 1
gauss(8)= 2
gauss(9)= 1
do k = 1,3
    do i = 2, h-1
        do j = 2, w-1
            l = 1
            summ = 0
            do ii = -1,1
                do jj = -1,1
                    summ = summ + img(i+ii, j+jj,k) * gauss(l)
                    l =l + 1
                end do
            end do
            blurImg(i-1,j-1,k) = summ / 16
        end do
    end do
end do
return
end subroutine

subroutine angle_rotate(img, angle, h, w, blurImg)
integer, intent(in) :: angle, h, w
integer, intent(in) :: img(h, w, 3)
integer, intent(out) :: blurImg(h, w, 3)
integer x0,y0,x,y

rad = 3.14159/(180.0/angle)

x0 = int(h/2)-1
y0 = int(w/2)-1

do k = 0,2
    do i =0,h-1
        do j = 0,w-1
            x = int((i-x0)*cos(rad) - (j-y0)*sin(rad) + x0)
            y = int((i-x0)*sin(rad) - (j-y0)*cos(rad) + y0)
            if ((x .lt. h) .and. (x .ge. 0)) then
                if ((y .lt. w) .and. (y .ge. 0)) blurImg(x+1, y+1, k+1) = img(i+1, j+1, k+1)
            end if
        end do
    end do
end do
return
end subroutine

subroutine sort(E, ns, med)
integer, intent(in):: ns
integer E(ns)
integer, intent(out) :: med
integer i,j,C

do i=1,ns
    do j=1,ns-1
        if(E(j+1).lt.E(j)) then
            C=E(j)
            E(j)=E(j+1)
            E(j+1)=C
        endif
    end do
end do
med = E((ns+1)/2)
return
end subroutine